var app = angular.module("app", ["ngRoute"]);

app.config(function($routeProvider, $httpProvider){
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    $routeProvider
        .when('/', {
            templateUrl:"viewsapp/partials/dashboard.html",
            controller: 'UserCtrl'
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

app.controller('UserCtrl', ['$scope', '$routeParams', function($scope, $routeParams) {
    $scope.test = 'this is a test message'
    console.log('controller running');
}])