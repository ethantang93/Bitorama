var app = angular.module("app", ["ngRoute", "djng.urls"]);

app.config(function($routeProvider, $httpProvider){
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $routeProvider
        .when('/', {
            templateUrl:"static/viewsapp/partials/dashboard.html"
        })
        .when('/login', {
            templateUrl:"partials/login.html"
        })
        .when('/register', {
            templateUrl:"partials/register.html"
        })
        .otherwise({
            redirect_to:"/"
        });
});

app.controller('UserCtrl', ['$scope', '$routeParams', '$location', 'UserFactory', function($scope, $routeParams, $location, UserFactory) {
    $scope.test = 'this is a test message'

    $scope.logout = function() {
        console.log('logout controller function');
        UserFactory.logout().success(function(response) {
            console.log(response);
            if(response.status) {
                $location.url('/');
            }
        }).error(function() {
            $location.url('/');
        })
    }
}])

app.factory('UserFactory', ['$http', '$routeParams', function ($http, $routeParams) {
    var factory = {};

    factory.logout = function() {
        console.log('logout factory function');
        return $http.get('/users/logout');
    }

    return factory;
}]);