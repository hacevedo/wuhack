var app = angular.module("crawlApp", []);

app.factory("apiService", function($http) {
	var apiResult = {};


	apiResult.getTopTen = function(loc, cat, sub_cat) {

		return data;
	};

	return apiResult;
});

app.controller("crawlCtrl",  ['$scope', '$http', 'apiService', function($scope, $http, apiService){
	$scope.categories = [
		{
			"name": "Attractions",
			"sub_categories" : [
				"Nightlife",
				"Bars",
				"Clubs",
				"Sightseeing Tours",
				"Performances",
				"Landmarks"
			]
		},
		{
			"name" : "Restaurants",
			"sub_categories" : [
				"Pub",
				"Bakery",
				"Chinese",
				"Sushi"
			]
		}
	];
	$scope.loc = "60763";
	$scope.cat = "attractions";
	$scope.sub_cat = "bars";
	$scope.num = "5";

	$scope.getResults = function (loc, cat, sub_cat){
		var url = "http://api.tripadvisor.com/api/partner/2.0/location/" + loc + "/" + cat + "?key=4FDDE1CDF4C2402980BABF84989B111D";
		if(sub_cat !== "") {
			url += "&subcategory=" +sub_cat;
		}
		console.log("here");

		$http.get(url).then(function(response){
			console.log("successful retrieval!");
			console.log(response);
			$scope.list= response.data.data;
		});

	};

	$scope.removePlace = function(index){
		$scope.list.splice(index,1);
	};
}]);