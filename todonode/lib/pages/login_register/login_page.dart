import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:get/instance_manager.dart';
import 'package:get/route_manager.dart';
import 'package:todonode/controllers/login.controller.dart';
import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area.dart';
import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area_object_class.dart';

class LoginPage extends ConsumerWidget {
  const LoginPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final emailController = ref.watch(emailControllerProvider);
    final passwordController = ref.watch(passwordControllerProvider);

    return Scaffold(
      body: Container(
        width: double.infinity,
        decoration: const BoxDecoration(
          image: DecorationImage(
            image:
                AssetImage('assets/Sea.jp'), // Set your background image here
            fit: BoxFit.fitHeight,
          ),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Welcome to Daily Blogs', // Change this to your app's name or slogan
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
            const SizedBox(height: 20),
            TextAreaWidget(
              viewmodel: emailObj,
              controller: emailController,
            ),
            const SizedBox(height: 20),
            TextAreaWidget(viewmodel: passwardObj,controller: passwordController),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Implement login functionality
              },
              child: const Text('Login'),
            ),
            TextButton(
              onPressed: () {
                Get.toNamed("/register");
              },
              child: const Text('Create an account'),
            ),
          ],
        ),
      ),
    );
  }
}
