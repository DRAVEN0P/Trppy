// ignore_for_file: public_member_api_docs, sort_constructors_first
import 'package:flutter/material.dart';
import 'package:flutter_material_symbols/flutter_material_symbols.dart';
import 'package:todonode/controllers/login.controller.dart';

// TextEditingController emailController = context.read(emailControllerProvider);


class TextAreaOb {
  final String hintText;
  final bool isObsecured;
  final TextEditingController controller;
  final TextInputType keyboardType;
  final Icon icon;

  TextAreaOb(
    this.hintText,
    this.isObsecured,
    this.controller,
    this.keyboardType,
    this.icon,
  );
}

final emailObj = TextAreaOb(
  "email",
  false,
  // emailControllerProvider,
  TextEditingController(),
  TextInputType.emailAddress,
  const Icon(
    MaterialSymbols.mail,
  ),
);

final passwardObj = TextAreaOb(
  "passward",
  true,
  TextEditingController(),
  TextInputType.text,
  const Icon(
    MaterialSymbols.lock,
  ),
);
final confirmPasswardObj = TextAreaOb(
  "confirm passward",
  true,
  TextEditingController(),
  TextInputType.text,
  const Icon(
    MaterialSymbols.lock,
  ),
);

final userObj = TextAreaOb(
  "name",
  false,
  TextEditingController(),
  TextInputType.text,
  const Icon(
    MaterialSymbols.person,
  ),
);
