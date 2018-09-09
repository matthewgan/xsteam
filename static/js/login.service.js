(function () {
    'use strict';

    var app = angular.module('xsteam.demo');
    app.service('LoginService',['$http', '$location', LoginService ]);

    function LoginService($http, $location) {
        this.login = login;
        this.isLoggedIn = isLoggedIn;
        this.logout = logout;
        this.redirectIfNotLoggedIn = redirectIfNotLoggedIn;

        function login(credentials) {
            return $http.post('auth_api/login/', credentials)
                .then(function(response) {
                    localStorage.currentUser = JSON.stringify(response.data);
                });
        }

        function isLoggedIn() {
            return !!localStorage.currentUser;
        }

        function logout() {
            delete localStorage.currentUser;
            $http.get('auth_api/logout')
                .then(function() {
                    $location.url('/login');
                });
        }

        function redirectIfNotLoggedIn() {
            if(!isLoggedIn()) {
                $location.url('/login');
            }
        }
    }
})();