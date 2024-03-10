import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:get/instance_manager.dart';
import 'package:get/route_manager.dart';
import 'package:todonode/models/places.dart';
import 'package:todonode/pages/home/wigets/place.container.dart';
import 'package:todonode/pages/sub_pages/list_places.dart';
import 'package:todonode/services/provider.dart';

class BeachPage extends ConsumerWidget {
  const BeachPage({super.key, required this.list});

  final AsyncValue<List<Places>> list;

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // AsyncValue<List<Places>> places = ref.watch(apiProvider);

    return list.when(
      loading: () => const Center(child: CircularProgressIndicator()),
      error: (error, stackTrace) => Text('Error: $error'),
      data: (placesList) {
        return Container(
          height: 370,
          child: ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: placesList.length,
              itemBuilder: (context, index) {
                return GestureDetector(
                    onTap: () {
                      if (placesList[index].name == "Goa") {
                        // print(placesList[index].name);
                        // Get.toNamed("/Goa");
                        Get.to(ListPlaces());
                      }
                    },
                    child: PlaceView(
                      obj: placesList[index],
                    ));
              }),
        );
      },
    );
  }
}

class TopDestinationView extends StatelessWidget {
  const TopDestinationView({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      child: const SingleChildScrollView(
        scrollDirection: Axis.horizontal,
        child: Row(children: [
          RecommendationPage(
            imgPath: "assets/beach/beach1.jpg",
          ),
          RecommendationPage(
            imgPath: "assets/beach/beach2.jpg",
          ),
          // PlaceView(),
        ]),
      ),
    );
  }
}
