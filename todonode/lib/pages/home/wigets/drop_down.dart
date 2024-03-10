import 'package:flutter/material.dart';
import 'package:flutter_material_symbols/flutter_material_symbols.dart';
import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area_constants.dart';

final textAreaBorderStyle = OutlineInputBorder(
  borderRadius: BorderRadius.circular(30),
  borderSide: BorderSide(
    color: NORMAL_COLOR,
    width: 1.0,
  ),
);

class SearchArea1 extends StatefulWidget {
  const SearchArea1({super.key, required this.controller});
  final TextEditingController controller;

  @override
  State<SearchArea1> createState() => _SearchArea1State();
}

class _SearchArea1State extends State<SearchArea1> {
  List<String> allplaces = places;
  @override
  Widget build(BuildContext context) {
    final height = MediaQuery.of(context).size.height;
    final width = MediaQuery.of(context).size.width;
    return Expanded(
      child: Container(
        width: double.infinity,
        // color: Colors.red,
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            TextFormField(
              controller: widget.controller,
              // keyboardType: viewmodel.keyboardType,
              cursorColor: Colors.grey,
              decoration: InputDecoration(
                contentPadding: const EdgeInsets.all(12.0),
                constraints: BoxConstraints(
                  maxHeight: height * 0.065,
                  maxWidth: width * 0.9,
                ),
                filled: true,
                fillColor: Colors.grey.shade200,
                hintText: " Search",
                border: textAreaBorderStyle,
                // --In Selected mode
                focusedBorder: textAreaBorderStyle.copyWith(
                    borderSide: const BorderSide(color: Colors.transparent)),
                // -- In normal mode
                enabledBorder: textAreaBorderStyle,
                prefixIcon: Icon(
                  MaterialSymbols.search,
                  color: Colors.grey.shade700,
                ),
              ),
              onChanged: searchPlace,
            ),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.only(left: 10.0, bottom: 0),
                child: ListView.builder(
                  itemCount: allplaces.length,
                  itemBuilder: (contex, index) {
                    return ListTile(
                      title: Text(allplaces[index]),
                    );
                  },
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  void searchPlace(String query) {
    final suggestions = places.where((element) {
      final place = element.toLowerCase();
      final input = query.toLowerCase();
      return place.contains(input);
    }).toList();

    setState(() {
      allplaces = suggestions;
    });
  }
}

final places = ["Delhi", "Mumbai", "Pune"];
