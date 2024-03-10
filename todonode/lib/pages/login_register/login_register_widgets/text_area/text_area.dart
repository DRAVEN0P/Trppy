import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:todonode/controllers/login.controller.dart';
import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area_constants.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area_object_class.dart';

// -- Style for the textfield
final textAreaBorderStyle = OutlineInputBorder(
  borderRadius: BorderRadius.circular(30),
  borderSide: BorderSide(
    color: NORMAL_COLOR,
    width: 1.0,
  ),
);

class TextAreaWidget extends StatelessWidget {
  const TextAreaWidget(
      {super.key, required this.viewmodel, required this.controller});
  final TextAreaOb viewmodel;
  final TextEditingController controller;

  @override
  Widget build(BuildContext context) {
    final height = MediaQuery.of(context).size.height;
    final width = MediaQuery.of(context).size.width;

    return TextFormField(
      controller: controller,
      obscureText: viewmodel.isObsecured,
      keyboardType: viewmodel.keyboardType,
      decoration: InputDecoration(
        // labelText: viewmodel.hintText,
        contentPadding: const EdgeInsets.all(12.0),
        constraints: BoxConstraints(
          maxHeight: height * 0.065,
          maxWidth: width * 0.9,
        ),
        filled: true,
        fillColor: Colors.white,
        hintText: viewmodel.hintText,
        border: textAreaBorderStyle,
        // --In Selected mode
        focusedBorder: textAreaBorderStyle.copyWith(
            borderSide: const BorderSide(color: FOCOUS_COLOR)),
        // -- In normal mode
        enabledBorder: textAreaBorderStyle,
        prefixIcon: viewmodel.icon,
      ),
    );
  }
}
