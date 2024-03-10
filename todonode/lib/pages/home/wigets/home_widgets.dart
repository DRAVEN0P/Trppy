import 'package:flutter/material.dart';
import 'package:todonode/pages/home/wigets/drop_down.dart';
import 'package:todonode/utils/text_widgets.dart';

// -- Style for the textfield
final textAreaBorderStyle = OutlineInputBorder(
  borderRadius: BorderRadius.circular(20),
  borderSide: const BorderSide(
    color: Colors.transparent,
    width: 1.0,
  ),
);

class SearchButton extends StatelessWidget {
  const SearchButton({super.key, required this.controller});
  final TextEditingController controller;

  @override
  Widget build(BuildContext context) {
    return IconButton(
          icon: const Icon(Icons.search),
          onPressed: () {
            showModalBottomSheet(
              context: context,
              backgroundColor: Colors.transparent,
              isScrollControlled: true,
              builder: (BuildContext context) {
                return DraggableScrollableSheet(
                  initialChildSize: 1.0,
                  minChildSize: 0.1,
                  maxChildSize: 1.0,
                  expand: true,
                  builder: (BuildContext context,
                      ScrollController scrollController) {
                    return Container(
                      // margin: EdgeInsets.only(top: 10),
                      color: Colors.white,
                      child: Padding(
                        padding: const EdgeInsets.only(top:80.0),
                        child: SearchArea1(controller: controller),
                      ),
                    );
                  },
                );
              },
            );
          },
        );
  }
}

List<Widget> top_seggestions = [
  TextButton(
    onPressed: () {},
    child: text18Normal(text: "Beachs"),
  ),
  SizedBox(width: 20,height: 1,),
  TextButton(
    onPressed: () {},
    child: text18Normal(text: "Mountains"),
  ),
  SizedBox(width: 20,height: 1,),
  TextButton(
    onPressed: () {},
    child: text18Normal(text: "Deserts"),
  ),
  SizedBox(width: 20,height: 1,),
  TextButton(
    onPressed: () {},
    child: text18Normal(text: "Religion"),
  ),
  SizedBox(width: 20,height: 1,),
];


