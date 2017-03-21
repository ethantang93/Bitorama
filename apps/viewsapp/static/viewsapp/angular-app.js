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
        .otherwise({
            redirect_to:"/"
        });
});

app.controller('UserCtrl', ['$scope', '$routeParams', '$location', 'UserFactory', function($scope, $routeParams, $location, UserFactory) {
    $scope.test = 'this is a test message';
    $scope.loginForm = {};

    $scope.login = function() {
        data = {
            'username': $scope.loginForm.username,
            'password': $scope.loginForm.password
        }
        UserFactory.login(data).then(function(response) {
            console.log(response.data);
            if (response.data.success) {
                $scope.loginForm ={};
                $location.url('/');
            } else {
                console.log(response.data[1]);
            }
        }).catch(function(response) {
            console.log("Errors: "+ response.data);
        });
        // $scope.loginForm = {};
    }

    $scope.logout = function() {
        UserFactory.logout().then(function(response) {
            console.log(response);
            if(response.status) {
                $location.url('/');
            }
        }).catch(function() {
            $location.url('/');
        });
    }
}])

app.factory('UserFactory', ['$http', '$routeParams', 'djangoUrl', function ($http, $routeParams, djangoUrl) {
    var factory = {};

    factory.login = function(data) {
        loginUrl = djangoUrl.reverse('users-app:login')
        return $http.post(loginUrl, data)
    }

    factory.logout = function() {
        logoutUrl = djangoUrl.reverse('users-app:logout')
        return $http.get(logoutUrl);
    }

    return factory;
}]);