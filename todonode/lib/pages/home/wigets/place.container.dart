import 'dart:collection';

import 'package:flutter/material.dart';
import 'package:todonode/models/places.dart';
import 'package:todonode/utils/text_widgets.dart';

class PlaceView extends StatelessWidget {
  const PlaceView({super.key, this.imgPath = "assets/Sea.jpg", required this.obj});

  final Places obj;

  final String imgPath;
  @override
  Widget build(
    BuildContext context,
  ) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
        // padding: EdgeInsets.all(10),
        decoration: BoxDecoration(
          image: DecorationImage(image: NetworkImage(obj.img), fit: BoxFit.cover),
          borderRadius: BorderRadius.circular(25),
        ),
        width: MediaQuery.of(context).size.width * 0.9,
        height: 370,
        child: Stack(
          children: [
            Positioned(
              child: _title(obj: obj,),
              bottom: 20,
              left: MediaQuery.of(context).size.width / 8,
            ),
          ],
        ),
      ),
    );
  }
}

class _title extends StatelessWidget {

  const _title({super.key, required this.obj});
  final Places obj;

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(40),
        color: Color.fromARGB(232, 255, 254, 254),
      ),
      width: 250,
      height: 100,
      child: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            text24Bold(text: obj.name),
            text16Normal(text: obj.desc)
          ],
        ),
      ),
    );
  }
}

class RecommendationPage extends StatelessWidget {
  const RecommendationPage({super.key, this.imgPath = "assets/Sea.jpg"});

  final String imgPath;
  @override
  Widget build(
    BuildContext context,
  ) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
        // padding: EdgeInsets.all(10),
        decoration: BoxDecoration(
          image: DecorationImage(image: AssetImage(imgPath), fit: BoxFit.cover),
          borderRadius: BorderRadius.circular(25),
        ),
        width: MediaQuery.of(context).size.width * 0.9,
        height: 150,
        // child: Stack(
        //   children: [
        //     Positioned(
        //       child: _title(),
        //       bottom: 20,
        //       left: MediaQuery.of(context).size.width / 8,
        //     ),
        //   ],
        // ),
      ),
    );
  }
}




