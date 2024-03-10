import 'package:get/route_manager.dart';
import 'package:todonode/pages/login_register/login_page.dart';
import 'package:todonode/pages/login_register/register_page.dart';
import 'package:todonode/pages/sub_pages/list_places.dart';

appRoutes() => [
      GetPage(
        name: '/login',
        page: () => const LoginPage(),
        transition: Transition.fade,
        transitionDuration: const Duration(milliseconds: 300),
      ),
      GetPage(
        name: '/register',
        page: () => const RegisterPage(),
        // middlewares: [MyMiddelware()],
        transition: Transition.fadeIn,
        transitionDuration: const Duration(milliseconds: 300),
      ),
      GetPage(
        name: '/Goa',
        page: () => const ListPlaces(),
        // middlewares: [MyMiddelware()],
        transition: Transition.fadeIn,
        transitionDuration: const Duration(milliseconds: 300),
      ),
    ];