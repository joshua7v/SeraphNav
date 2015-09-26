angular.module('app', ['ngMaterial'])
.controller('Controller', function($scope, $timeout, $mdSidenav, $mdUtil, $log) {

    $scope.site = {
      title: '',
      desc: '',
      url: 'http://',
      category: {
          name: ''
      }
    };

//    $scope.category = null;
    $scope.categories = null;
    $scope.loadCategories = function() {

        return (function () {
            var xhr = new XMLHttpRequest();
            xhr.open('GET', '/categories', true);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == 4 && xhr.status == 200) {
                    console.log(xhr.responseText);
                    $scope.categories = $scope.categories || JSON.parse(xhr.responseText);

                }
            };

            if (!$scope.categories) {
                xhr.send();
            }

        })();
    };

    $scope.selectClose = function () {
        $('#select_value_label_0 > span:nth-child(1)').text('▶ Select ◀️');
    };
});
