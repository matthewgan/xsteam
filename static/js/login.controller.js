(function () {
    'use strict';

    var app = angular.module('xsteam.demo');
    app.controller('LoginController',['$scope', '$http', '$location', 'LoginService', LoginController ]);

    function LoginController($scope, $http, $location, LoginService) {
        $scope.login = function() {
            LoginService.login($scope.user)
                .then(function() {
                    $location.url('/');
                },
                function() {
                    $scope.login_error="Invalid username or password.";
                });
        }

        if(LoginService.isLoggedIn()) {
            $location.url('/');
        }
    }
})();