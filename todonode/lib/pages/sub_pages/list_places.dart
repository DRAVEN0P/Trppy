import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:todonode/models/places.dart';
import 'package:todonode/pages/sub_pages/beaches.dart';
import 'package:todonode/services/provider.dart';
import 'package:todonode/utils/text_widgets.dart';

// class ListPlaces extends ConsumerWidget {
//   const ListPlaces({super.key});

//   @override
//   Widget build(BuildContext context,WidgetRef ref) {

//     AsyncValue<List<Places>> places = ref.watch(apiProvider);
    
//     return Scaffold(
//       body: Expanded(
//         flex: 1,
//         child: SingleChildScrollView(
//           child: Container(
//             margin: EdgeInsets.only(top: 60),
//             child: Column(crossAxisAlignment: CrossAxisAlignment.start,children: [
//               Padding(
//                 padding: const EdgeInsets.only(left: 20),
//                 child: text24Bold(text: "Goa"),
//               ),
//               SizedBox(height: 20,),
//               Padding(
//                 padding: const EdgeInsets.only(left: 20),
//                 child: text24Bold(text: "Places"),
//               ),
//               BeachPage(list: places,),
//               Padding(
//                 padding: const EdgeInsets.only(left: 20),
//                 child: text24Bold(text: "Foods"),
//               ),
//               BeachPage(list: places,),
//             ]),
//           ),
//         ),
//       ),
//     );
//   }
// }

class ListPlaces extends ConsumerWidget {
  const ListPlaces({super.key});

  @override
  Widget build(BuildContext context,WidgetRef ref) {

    AsyncValue<List<Places>> places = ref.watch(apiProvider);
    
    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
          margin: EdgeInsets.only(top: 60),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start,children: [
            Padding(
              padding: const EdgeInsets.only(left: 20),
              child: text24Bold(text: "Goa"),
            ),
            SizedBox(height: 20,),
            Padding(
              padding: const EdgeInsets.only(left: 20),
              child: text24Bold(text: "Places"),
            ),
            BeachPage(list: places,),
            Padding(
              padding: const EdgeInsets.only(left: 20),
              child: text24Bold(text: "Foods"),
            ),
            BeachPage(list: places,),
          ]),
        ),
      ),
    );
  }
}
