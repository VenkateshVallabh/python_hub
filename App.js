// app.js

angular.module('portfolioApp', [])
    .controller('MainController', function($scope) {
        $scope.formData = {};

        $scope.submitForm = function() {
            // Handle form submission here
            console.log($scope.formData); // Example: Log form data to the console
            // You can add AJAX request or any other logic for form submission here
            // Reset form after submission (optional)
            $scope.formData = {};
        };
    });
