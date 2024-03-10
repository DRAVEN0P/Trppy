import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:todonode/models/places.dart';
import 'package:todonode/pages/home/wigets/appbar.dart';
import 'package:todonode/pages/home/wigets/home_widgets.dart';
import 'package:todonode/pages/sub_pages/beaches.dart';
import 'package:todonode/services/provider.dart';
import 'package:todonode/utils/text_widgets.dart';

class HomePage extends ConsumerWidget {
  const HomePage({super.key});
  @override
  Widget build(BuildContext context,WidgetRef ref) {
    TextEditingController searchController = TextEditingController();
    AsyncValue<List<Places>> places = ref.watch(apiProvider);

    return Scaffold(
      body: Container(
        margin: const EdgeInsets.only(top: 60),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            CustomAppBar(
              controller: searchController,
            ),
            const SizedBox(height: 10),
            SingleChildScrollView(
              scrollDirection: Axis.horizontal,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceAround,
                mainAxisSize: MainAxisSize.max,
                children: top_seggestions,
              ),
            ),
            BeachPage(list: places),
            Padding(
              padding: const EdgeInsets.only(left: 15),
              child: text24Bold(text: "Top Destinations"),
            ),
            const TopDestinationView(),
          ],
        ),
      ),
    );
  }
}
