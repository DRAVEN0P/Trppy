import 'package:flutter/material.dart';
import 'package:todonode/pages/home/wigets/home_widgets.dart';

class CustomAppBar extends StatelessWidget {
  const CustomAppBar({super.key, required this.controller});
  final TextEditingController controller;
  @override
  Widget build(BuildContext context) {
    return Container(
      // color: Colors.red,
      padding: const EdgeInsets.only(left: 20, right: 20),
      height: 30,
      width: double.infinity,
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        // crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          const Text(
            "Discover",
            style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
          ),
          Row(
            children: [
              SearchButton(controller: controller,),
              IconButton(
                onPressed: () {},
                icon: Icon(Icons.notifications),
              ),
              
            ],
          )
        ],
      ),
    );
  }
}
