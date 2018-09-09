(function(){
    'use strict';

    var app = angular.module('xsteam.demo', ['ngRoute']);

    app.config(['$routeProvider', config]).run(['$http', AppRun]);
    app.controller('XsteamController',[ '$scope', '$http', '$location', 'LoginService', XsteamController ]);

    function config($routeProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'static/html/home.html',
                controller: 'XsteamController',
            })
            .when('/login', {
                templateUrl: 'static/html/login.html',
                controller: 'LoginController',
            })
            .otherwise('/');
    }

    function AppRun($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken'
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

    function XsteamController($scope, $http, $location, LoginService) {

        LoginService.redirectIfNotLoggedIn();
        $scope.logout = LoginService.logout;
        //$scope.sortBy = 'story_points';
        $scope.reverse = true;
        $scope.showFilters = false;

        $scope.add = function(list, title) {
            var card = {
                list: list.id,
                title: title
            };

            $http.post('/scrumboard/cards/', card)
            .then(
                function(response){
                    list.cards.push(response.data);
                },
                function(){ //Error handling
                    alert('Could not create card')
                }
            );

        };

        $scope.data = [];
        $http.get('/scrumboard/lists/').then(function(response){
            $scope.data = response.data;
        });
    }
}());