import 'package:flutter/material.dart';
import 'package:todonode/utils/app_colors.dart';

Widget text24Bold({String text = "",Color color = AppColors.primaryText}) {
  return Text(
    text,
    style: TextStyle(
      color: color,
      fontSize: 24,
      fontWeight: FontWeight.bold,
    ),
    textAlign: TextAlign.center,
  );
}

Widget text16Normal({String text = "",Color color = AppColors.primaryText}) {
  return Text(
    text,
    style: TextStyle(
      color: color,
      fontSize: 16,
      fontWeight: FontWeight.normal,
    ),
    textAlign: TextAlign.center,
  );
}
Widget text18Normal({String text = "",Color color = AppColors.primaryText}) {
  return Text(
    text,
    style: TextStyle(
      color: color,
      fontSize: 18,
      fontWeight: FontWeight.normal,
    ),
    textAlign: TextAlign.center,
  );
}