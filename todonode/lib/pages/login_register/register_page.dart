import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:get/instance_manager.dart';
import 'package:get/route_manager.dart';
import 'package:todonode/controllers/login.controller.dart';
import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area.dart';
import 'package:todonode/pages/login_register/login_register_widgets/text_area/text_area_object_class.dart';

class RegisterPage extends ConsumerWidget {
  const RegisterPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    //Controllers injected
    final nameController = ref.watch(registerNameControllerProvider);
    final emailController = ref.watch(registerEmailControllerProvider);
    final passwordController = ref.watch(registerPasswordControllerProvider);
    final confirmPasswordController =
        ref.watch(registerConfirmPasswordControllerProvider);

    return Scaffold(
      body: Container(
        width: double.infinity,
        decoration: const BoxDecoration(
          image: DecorationImage(
            image:
                AssetImage('assets/bg.jpg'), // Set your background image here
            fit: BoxFit.fitHeight,
          ),
        ),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Register', // Change this to your app's name or slogan
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Colors.white,
              ),
            ),
            const SizedBox(height: 20),
            TextAreaWidget(
              viewmodel: userObj,
              controller: nameController,
            ),
            const SizedBox(height: 20),
            TextAreaWidget(
              viewmodel: emailObj,
              controller: emailController,
            ),
            const SizedBox(height: 20),
            TextAreaWidget(
              viewmodel: passwardObj,
              controller: passwordController,
            ),
            const SizedBox(height: 20),
            TextAreaWidget(
              viewmodel: confirmPasswardObj,
              controller: confirmPasswordController,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Implement login functionality
              },
              child: const Text('Create Account'),
            ),
            TextButton(
              onPressed: () {
                Get.toNamed("/login");
              },
              child: const Text('Already have Account'),
            ),
          ],
        ),
      ),
    );
  }
}
