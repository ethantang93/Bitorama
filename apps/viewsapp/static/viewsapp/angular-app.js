var app = angular.module("app", ["ngRoute", "djng.urls"]);

app.config(function($routeProvider, $httpProvider){
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $routeProvider
        .when('/', {
            templateUrl:"static/viewsapp/partials/dashboard.html"
        })
        .when('/login', {
            templateUrl:"static/viewsapp/partials/login.html"
        })
        .when('/register', {
            templateUrl:"static/viewsapp/partials/register.html"
        })
        .when('/items', {
            templateUrl:"static/viewsapp/partials/items.html"
        })
        .otherwise({
            redirect_to:"/"
        });
});

app.controller('UserCtrl', ['$scope', '$routeParams', '$location', 'UserFactory', function($scope, $routeParams, $location, UserFactory) {
    $scope.test = 'this is a test message';
    $scope.loginForm = {};
    $scope.regForm = {};
    $scope.user = null;

    checkLogin = function() {
        UserFactory.checkLogin().then(function(response) {
            console.log(response);
            if (response.data.success) {
                console.log('the tales were true. a user is here');
                $scope.user = response.data.user;
                console.log($scope.user);
            }
        })
    };
    checkLogin();

    $scope.login = function() {
        var data = {
            'username': $scope.loginForm.username,
            'password': $scope.loginForm.password
        };
        UserFactory.login(data).then(function(response) {
            console.log(response.data);
            if (response.data.success) {
                $scope.user = response.data.user
                $scope.loginForm ={};
                $location.url('/');
            } else {
                console.log(response.data[1]);
            }
        }).catch(function(response) {
            console.log("Errors: "+ response.data);
        });
        // $scope.loginForm = {};
    };

    $scope.register = function(){
          var data = {
            'username':$scope.regForm.username,
            'email':$scope.regForm.email,
            'first_name':$scope.regForm.first_name,
            'last_name':$scope.regForm.last_name,
            'password':$scope.regForm.password,
            'confirm_pw':$scope.regForm.confirm_pw
          };
          UserFactory.register(data).then(function(response){
            console.log(response.data);
            if (response.data.success) {
                $scope.user = response.data.user;
                $scope.regForm ={};
                $location.url('/');
            }else{
                console.log(response.data[1])
            }
          })
    };
    $scope.logout = function() {
        UserFactory.logout().then(function(response) {
            if(response.status) {
                $scope.user = null;
                $location.url('/');
            }
        }).catch(function() {
            $location.url('/');
        });
    }
}]);

app.factory('UserFactory', ['$http', '$routeParams', 'djangoUrl', function ($http, $routeParams, djangoUrl) {
    var factory = {};

    factory.checkLogin = function() {
        checkLoginUrl = djangoUrl.reverse('users-app:check_login');
        return $http.get(checkLoginUrl);
    };

    factory.login = function(data) {
        loginUrl = djangoUrl.reverse('users-app:login');
        return $http.post(loginUrl, data);
    };

    factory.register = function(data){
        registerUrl = djangoUrl.reverse('users-app:register');
        return $http.post(registerUrl, data);
    };

    factory.logout = function() {
        logoutUrl = djangoUrl.reverse('users-app:logout');
        return $http.get(logoutUrl);
    };

    return factory;
}]);

app.controller('ItemCtrl', ['$scope', '$routeParams', '$location', 'ItemFactory', function($scope, $routeParams, $location, ItemFactory) {
    $scope.itemForm={};
    ItemFactory.item_index().then(function(response){
        $scope.items = response.data.items
        console.log($scope.items);
    });
    $scope.create_item = function(){
        var data = {
            'item_name':$scope.itemForm.name,
            'price':$scope.itemForm.price,
            'description':$scope.itemForm.description,
            'seller':$scope.user,
            'quantity':$scope.itemForm.quantity
        };
        ItemFactory.create_item(data).then(function(response){
          console.log(response.data);
          if (response.data.success) {
              $scope.itemForm ={};
              $location.url('/items');
              $scope.items.push(response.data.item)
          }else{
              console.log("doesnt work");
          }
        })
    }
}]);

app.factory('ItemFactory',['$http','$routeParams','djangoUrl',function($http, $routeParams, djangoUrl){
    var factory = {};
    factory.item_index = function(){
        url = djangoUrl.reverse('items-app:item_index');
        return $http.post(url)
    };
    factory.create_item = function(data){
        Url = djangoUrl.reverse('items-app:create_item');
        return $http.post(Url, data)
    };
    return factory;
}]);
