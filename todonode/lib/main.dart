import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:get/route_manager.dart';
import 'package:todonode/pages/home/home_page.dart';
import 'package:todonode/pages/home/wigets/drop_down.dart';
import 'package:todonode/pages/login_register/login_page.dart';
import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area_constants.dart';
import 'package:todonode/pages/sub_pages/beaches.dart';
import 'package:todonode/pages/sub_pages/list_places.dart';
import 'package:todonode/utils/routes.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      // routes: appRoutes(),
      initialRoute: "/",
      getPages: appRoutes(),
      theme: ThemeData(
        primarySwatch: FOCOUS_COLOR,
      ),
      home: HomePage(),
    );
  }
}



