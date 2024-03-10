import 'dart:convert';

import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:todonode/models/places.dart';
import 'package:http/http.dart' as http;


final apiProvider = FutureProvider.autoDispose<List<Places>>((ref) async {
  // Simulating a network call with a delay
  await Future.delayed(Duration(seconds: 2));

  var response = await http.get(Uri.parse("http://localhost:8000/allBeaches"));
  
  // print(response.body);

  if (response.statusCode == 200) {

    List<Places> placesList = [];
    var jsonData = json.decode(response.body);
    jsonData = jsonData["AllBeaches"];

    for (var i = 0; i < jsonData.length; i++) {
      var name = jsonData[i]["name"];
      var img = jsonData[i]["img"];
      var desc = jsonData[i]["desc"];
      var temp = Places(name, img,desc);

      placesList.add(temp);
    }
    // print(placesList);
    return placesList;
  } else {
    // If the server did not return a 200 OK response, throw an exception
    throw Exception('Failed to load data');
  }

  // Replace this with your actual API call
  // For demonstration purposes, returning a list of strings
  // return [];
});