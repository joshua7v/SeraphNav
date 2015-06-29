angular.module('app', ['ngMaterial']).controller('Controller', function($scope, $timeout, $mdSidenav, $mdUtil, $log) {
    $scope.msg = 'hhh';
    $scope.googleUrl = 'xxx';
    $scope.toggleRight = buildToggler('right');
    function buildToggler(navID) {
        var debounceFn =  $mdUtil.debounce(function(){
            $mdSidenav(navID)
                .toggle()
                .then(function () {
                    $log.debug("toggle " + navID + " is done");
                });
        },300);
        return debounceFn;
    }
    $scope.site = {
      title: '',
      desc: '',
      url: 'http://'
    };
})
    .controller('RightCtrl', function ($scope, $timeout, $mdSidenav, $log) {
        $scope.close = function () {
            $mdSidenav('right').close()
                .then(function () {
                    $log.debug("close RIGHT is done");
                });
        };
    });