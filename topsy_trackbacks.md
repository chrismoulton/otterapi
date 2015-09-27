**Request**: `http://otter.topsy.com/trackbacks.txt?tracktype=tweet__trackback&url=http%3A%2F%2Ftopsy.com%2F&apikey=<your_apikey>`

**Response**: The TXT response is shown below. Other [response formats](ResponseFormats.md) are also available.

```
### FOR DEBUG ONLY ###
$VAR1 = {
          'request' => {
                         'resource' => 'trackbacks',
                         'response_type' => 'txt',
                         'parameters' => {
                                           'url' => 'http://topsy.com/',
                                           'tracktype' => 'tweet__trackback'
                                         },
                         'url' => 'http://otter.topsy.com/trackbacks.txt?tracktype=tweet__trackback&url=http%3A%2F%2Ftopsy.com%2F'
                       },
          'response' => {
                          'page' => 1,
                          'total' => 500,
                          'trackback_total' => 13783,
                          'perpage' => 10,
                          'last_offset' => 10,
                          'topsy_trackback_url' => 'http://topsy.com/topsy.com/',
                          'hidden' => 0,
                          'offset' => 0,
                          'list' => [
                                      {
                                        'permalink_url' => 'http://twitter.com/stanley_n_ky/status/280731443079020545',
                                        'date' => 1355766566,
                                        'content' => 'Y&#39;all can pull up your tweeter stats on http://t.co/XXcZ4VOX its a good site',
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/stanley_n_ky',
                                                      'name' => 'Stanley',
                                                      'nick' => 'stanley_n_ky',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2883450669/875707419582f8e0e3758d1a2e53f38d_normal.jpeg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/stanley_n_ky?utm_source=otter',
                                                      'influence_level' => 8
                                                    },
                                        'date_alpha' => '2 hours ago',
                                        'highlight' => 'Y&#39;all can pull up your tweeter stats on http://t.co/XXcZ4VOX its a good site '
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/wshama/status/280691766674456576',
                                        'date' => 1355757106,
                                        'content' => "\@SawsanDoula \x{d9}\x{85}\x{d9}\x{86} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d8}\x{a7}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d8}\x{ac}\x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{8a}\x{d8}\x{a9}...\x{d9}\x{87}\x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a8}\x{d8}\x{b4}\x{d9}\x{88}\x{d9}\x{81} \x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{87} \x{d8}\x{a7}\x{d9}\x{84}\x{d8}\x{a3}\x{d9}\x{81}\x{d8}\x{b6}\x{d9}\x{84} \x{d8}\x{a8}\x{d8}\x{ae}\x{d8}\x{b5}\x{d9}\x{88}\x{d8}\x{b5} \x{d8}\x{b7}\x{d9}\x{84}\x{d8}\x{a8}\x{d9}\x{83} http://t.co/X98OyU1G",
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/wshama',
                                                      'name' => 'Shamma',
                                                      'nick' => 'wshama',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2982607488/d40173eaca0221f46a0a758f35836231_normal.jpeg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/wshama?utm_source=otter'
                                                    },
                                        'date_alpha' => '5 hours ago',
                                        'highlight' => "\@SawsanDoula \x{d9}\x{85}\x{d9}\x{86} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d8}\x{a7}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d8}\x{ac}\x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{8a}\x{d8}\x{a9}...\x{d9}\x{87}\x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a8}\x{d8}\x{b4}\x{d9}\x{88}\x{d9}\x{81} \x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{87} \x{d8}\x{a7}\x{d9}\x{84}\x{d8}\x{a3}\x{d9}\x{81}\x{d8}\x{b6}\x{d9}\x{84} \x{d8}\x{a8}\x{d8}\x{ae}\x{d8}\x{b5}\x{d9}\x{88}\x{d8}\x{b5} \x{d8}\x{b7}\x{d9}\x{84}\x{d8}\x{a8}\x{d9}\x{83} http://t.co/X98OyU1G "
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/maathmusleh/status/280667947255615488',
                                        'date' => 1355751427,
                                        'content' => "\@SawsanDoula \x{d9}\x{85}\x{d9}\x{86} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d8}\x{a7}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d8}\x{ac}\x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{8a}\x{d8}\x{a9}...\x{d9}\x{87}\x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a8}\x{d8}\x{b4}\x{d9}\x{88}\x{d9}\x{81} \x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{87} \x{d8}\x{a7}\x{d9}\x{84}\x{d8}\x{a3}\x{d9}\x{81}\x{d8}\x{b6}\x{d9}\x{84} \x{d8}\x{a8}\x{d8}\x{ae}\x{d8}\x{b5}\x{d9}\x{88}\x{d8}\x{b5} \x{d8}\x{b7}\x{d9}\x{84}\x{d8}\x{a8}\x{d9}\x{83} http://t.co/X98OyU1G",
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/maathmusleh',
                                                      'name' => 'Maath Musleh',
                                                      'nick' => 'maathmusleh',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2971103671/109ef00e3208c1e4e340636a949072eb_normal.jpeg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/maathmusleh?utm_source=otter'
                                                    },
                                        'date_alpha' => '7 hours ago',
                                        'highlight' => "\@SawsanDoula \x{d9}\x{85}\x{d9}\x{86} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d8}\x{a7}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d8}\x{ac}\x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{8a}\x{d8}\x{a9}...\x{d9}\x{87}\x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{85}\x{d9}\x{88}\x{d9}\x{82}\x{d8}\x{b9} \x{d8}\x{a8}\x{d8}\x{b4}\x{d9}\x{88}\x{d9}\x{81} \x{d8}\x{a7}\x{d9}\x{86}\x{d9}\x{87} \x{d8}\x{a7}\x{d9}\x{84}\x{d8}\x{a3}\x{d9}\x{81}\x{d8}\x{b6}\x{d9}\x{84} \x{d8}\x{a8}\x{d8}\x{ae}\x{d8}\x{b5}\x{d9}\x{88}\x{d8}\x{b5} \x{d8}\x{b7}\x{d9}\x{84}\x{d8}\x{a8}\x{d9}\x{83} http://t.co/X98OyU1G ",
                                        'permalink' => {
                                                         'topsy_trackback_url' => 'http://topsy.com/topsy.com/?utm_source=otter',
                                                         'trackback_total' => 1
                                                       }
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/safsofafa/status/280647147882422272',
                                        'date' => 1355746468,
                                        'content' => "\@AmiraTahers \x{d9}\x{84}\x{d9}\x{88}\x{d8}\x{b9}\x{d8}\x{a7}\x{d9}\x{8a}\x{d8}\x{b2}\x{d9}\x{87} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{aa}\x{d9}\x{83} \x{d9}\x{83}\x{d9}\x{84}\x{d9}\x{87}\x{d8}\x{a7} \x{d9}\x{85}\x{d9}\x{86} \x{d8}\x{b3}\x{d8}\x{a7}\x{d8}\x{b9}\x{d9}\x{87} \x{d9}\x{85}\x{d8}\x{a7} \x{d8}\x{a8}\x{d8}\x{af}\x{d8}\x{a3}\x{d8}\x{aa}\x{d9}\x{8a} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{b1}..\x{d8}\x{a3}\x{d9}\x{88} \x{d8}\x{a3}\x{d8}\x{b1}\x{d8}\x{b4}\x{d9}\x{8a}\x{d9}\x{81} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{aa} \x{d8}\x{a3}\x{d9}\x{8a} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{a8}..\x{d8}\x{a7}\x{d8}\x{af}\x{d8}\x{ae}\x{d9}\x{84}\x{d9}\x{8a} \x{d8}\x{b9}\x{d9}\x{84}\x{d9}\x{8a} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{84}\x{d9}\x{8a}\x{d9}\x{86}\x{d9}\x{83} \x{d8}\x{af}\x{d9}\x{87}..\x{d8}\x{aa}\x{d8}\x{ad}\x{d9}\x{8a}\x{d8}\x{a7}\x{d8}\x{aa}\x{d9}\x{8a} \x{d9}\x{84}\x{d9}\x{8a}\x{d9}\x{83}\x{d9}\x{8a} :)  http://t.co/wBFPlTEp",
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/safsofafa',
                                                      'name' => 'safsaf',
                                                      'nick' => 'safsofafa',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2971755517/7bc4a5e5df875b697ec552bc136f0a4d_normal.jpeg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/safsofafa?utm_source=otter'
                                                    },
                                        'date_alpha' => '8 hours ago',
                                        'highlight' => "\@AmiraTahers \x{d9}\x{84}\x{d9}\x{88}\x{d8}\x{b9}\x{d8}\x{a7}\x{d9}\x{8a}\x{d8}\x{b2}\x{d9}\x{87} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{aa}\x{d9}\x{83} \x{d9}\x{83}\x{d9}\x{84}\x{d9}\x{87}\x{d8}\x{a7} \x{d9}\x{85}\x{d9}\x{86} \x{d8}\x{b3}\x{d8}\x{a7}\x{d8}\x{b9}\x{d9}\x{87} \x{d9}\x{85}\x{d8}\x{a7} \x{d8}\x{a8}\x{d8}\x{af}\x{d8}\x{a3}\x{d8}\x{aa}\x{d9}\x{8a} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{b1}..\x{d8}\x{a3}\x{d9}\x{88} \x{d8}\x{a3}\x{d8}\x{b1}\x{d8}\x{b4}\x{d9}\x{8a}\x{d9}\x{81} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{aa} \x{d8}\x{a3}\x{d9}\x{8a} \x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{a8}..\x{d8}\x{a7}\x{d8}\x{af}\x{d8}\x{ae}\x{d9}\x{84}\x{d9}\x{8a} \x{d8}\x{b9}\x{d9}\x{84}\x{d9}\x{8a} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{84}\x{d9}\x{8a}\x{d9}\x{86}\x{d9}\x{83} \x{d8}\x{af}\x{d9}\x{87}..\x{d8}\x{aa}\x{d8}\x{ad}\x{d9}\x{8a}\x{d8}\x{a7}\x{d8}\x{aa}\x{d9}\x{8a} \x{d9}\x{84}\x{d9}\x{8a}\x{d9}\x{83}\x{d9}\x{8a} :)  http://t.co/wBFPlTEp "
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/nachexpac/status/280644144286801921',
                                        'date' => 1355745752,
                                        'content' => '@s_lehuede http://t.co/uBtKlBYo es como lo mejorcito',
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/nachexpac',
                                                      'name' => 'Ignacio Correa',
                                                      'nick' => 'nachexpac',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2957001998/5aa8e1aedb8b483b1698e2ed0fb9654f_normal.png',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/nachexpac?utm_source=otter',
                                                      'influence_level' => 7
                                                    },
                                        'date_alpha' => '8 hours ago',
                                        'highlight' => '@s_lehuede http://t.co/uBtKlBYo es como lo mejorcito '
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/iluvag13/status/280640587512819712',
                                        'date' => 1355744904,
                                        'content' => '@ArianaGroxmysox oh. Go on http://t.co/TspbYCry you can look at her old tweets even if she deleted it:))',
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/iluvag13',
                                                      'name' => "Lexie\x{e2}\x{99}\x{a5}",
                                                      'nick' => 'iluvag13',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2896527967/561927a062e6b4f15745b14d40ec78b9_normal.jpeg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/iluvag13?utm_source=otter'
                                                    },
                                        'date_alpha' => '8 hours ago',
                                        'highlight' => '@ArianaGroxmysox oh. Go on http://t.co/TspbYCry you can look at her old tweets even if she deleted it:)) '
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/gallopingslut/status/280640397603110912',
                                        'date' => 1355744859,
                                        'content' => '@daehlers http://t.co/4gr5bNWp OMf',
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/gallopingslut',
                                                      'name' => 'confused tbh -5',
                                                      'nick' => 'gallopingslut',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2984408470/58575d78473cb59fd01221fc438a23e8_normal.png',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/gallopingslut?utm_source=otter'
                                                    },
                                        'date_alpha' => '9 hours ago',
                                        'highlight' => '@daehlers http://t.co/4gr5bNWp OMf '
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/a7madelmasry/status/280622546230079489',
                                        'date' => 1355740603,
                                        'content' => "\@Masr \x{d9}\x{84}\x{d9}\x{82}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{ad}\x{d8}\x{af} \x{d8}\x{b9}\x{d8}\x{a7}\x{d9}\x{85}\x{d9}\x{84}\x{d9}\x{87}\x{d8}\x{a7} \x{d8}\x{b1}\x{d9}\x{8a}\x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{b9}\x{d8}\x{a7}\x{d9}\x{84}\x{d8}\x{aa}\x{d8}\x{a7}\x{d9}\x{8a}\x{d9}\x{85}\x{d9}\x{84}\x{d8}\x{a7}\x{d9}\x{8a}\x{d9}\x{86} :)) .. \x{d8}\x{a8}\x{d8}\x{af}\x{d9}\x{88}\x{d8}\x{b1} \x{d9}\x{84}\x{d9}\x{82}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{a8}\x{d8}\x{b3}\x{d8}\x{a7}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{af}\x{d8}\x{a9} \x{d8}\x{a8}\x{d8}\x{b3} \x{d9}\x{85}\x{d8}\x{b4} \x{d8}\x{b9}\x{d8}\x{a7}\x{d8}\x{b1}\x{d9}\x{81} \x{d8}\x{a7}\x{d9}\x{88}\x{d8}\x{b5}\x{d9}\x{84} \x{d9}\x{84}\x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{aa}\x{d9}\x{89} \x{d9}\x{85}\x{d9}\x{86}\x{d8}\x{a9} http://t.co/kNUqnwhf",
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/a7madelmasry',
                                                      'name' => "\x{d9}\x{85}\x{d8}\x{b5}\x{d8}\x{b1}\x{d9}\x{89}",
                                                      'nick' => 'a7madelmasry',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2688478343/eaab5664597b8f32fa6d422afa88da56_normal.jpeg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/a7madelmasry?utm_source=otter'
                                                    },
                                        'date_alpha' => '10 hours ago',
                                        'highlight' => "\@Masr \x{d9}\x{84}\x{d9}\x{82}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{ad}\x{d8}\x{af} \x{d8}\x{b9}\x{d8}\x{a7}\x{d9}\x{85}\x{d9}\x{84}\x{d9}\x{87}\x{d8}\x{a7} \x{d8}\x{b1}\x{d9}\x{8a}\x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{b9}\x{d8}\x{a7}\x{d9}\x{84}\x{d8}\x{aa}\x{d8}\x{a7}\x{d9}\x{8a}\x{d9}\x{85}\x{d9}\x{84}\x{d8}\x{a7}\x{d9}\x{8a}\x{d9}\x{86} :)) .. \x{d8}\x{a8}\x{d8}\x{af}\x{d9}\x{88}\x{d8}\x{b1} \x{d9}\x{84}\x{d9}\x{82}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{a7}\x{d9}\x{84}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{a8}\x{d8}\x{b3}\x{d8}\x{a7}\x{d9}\x{8a}\x{d8}\x{aa} \x{d8}\x{af}\x{d8}\x{a9} \x{d8}\x{a8}\x{d8}\x{b3} \x{d9}\x{85}\x{d8}\x{b4} \x{d8}\x{b9}\x{d8}\x{a7}\x{d8}\x{b1}\x{d9}\x{81} \x{d8}\x{a7}\x{d9}\x{88}\x{d8}\x{b5}\x{d9}\x{84} \x{d9}\x{84}\x{d8}\x{aa}\x{d9}\x{88}\x{d9}\x{8a}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{aa}\x{d9}\x{89} \x{d9}\x{85}\x{d9}\x{86}\x{d8}\x{a9} http://t.co/kNUqnwhf "
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/naizmudin/status/280621163355455488',
                                        'date' => 1355740273,
                                        'content' => "RT #filternet Twitter Trackbacks for \x{d8}\x{a7}\x{d9}\x{86}\x{da}\x{88}\x{d9}\x{88}\x{d9}\x{86}\x{db}\x{8c}\x{d8}\x{b4}\x{db}\x{8c}\x{d8}\x{a7} \x{d9}\x{85}\x{db}\x{8c}\x{da}\x{ba} \x{d8}\x{ac}\x{d8}\x{b9}\x{d9}\x{84}\x{db}\x{8c} \x{d9}\x{86}\x{d8}\x{a8}\x{db}\x{8c} \x{da}\x{af}\x{d8}\x{b1}\x{d9}\x{81}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{b1} [http://t.co/EEWZpr8F] on http://t.co/a0ST9I5x http://t.co/1RkOqgm4",
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/naizmudin',
                                                      'name' => 'Naizmudin',
                                                      'nick' => 'naizmudin',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/1861028029/207px-Nima_Yushij_-_Original_normal.jpg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/naizmudin?utm_source=otter'
                                                    },
                                        'date_alpha' => '10 hours ago',
                                        'highlight' => "RT <a href=\"http://topsy.com/s?q=%23filternet&utm_source=ottertag\">#filternet</a> Twitter Trackbacks for \x{d8}\x{a7}\x{d9}\x{86}\x{da}\x{88}\x{d9}\x{88}\x{d9}\x{86}\x{db}\x{8c}\x{d8}\x{b4}\x{db}\x{8c}\x{d8}\x{a7} \x{d9}\x{85}\x{db}\x{8c}\x{da}\x{ba} \x{d8}\x{ac}\x{d8}\x{b9}\x{d9}\x{84}\x{db}\x{8c} \x{d9}\x{86}\x{d8}\x{a8}\x{db}\x{8c} \x{da}\x{af}\x{d8}\x{b1}\x{d9}\x{81}\x{d8}\x{aa}\x{d8}\x{a7}\x{d8}\x{b1} [http://t.co/EEWZpr8F] on http://t.co/a0ST9I5x http://t.co/1RkOqgm4 "
                                      },
                                      {
                                        'permalink_url' => 'http://twitter.com/thea_17forever/status/280585902194040832',
                                        'date' => 1355731866,
                                        'content' => 'i can&#39;t find any of the links!! http://t.co/XhPP829K WORK YOUR MAGIC',
                                        'type' => 'tweet',
                                        'author' => {
                                                      'url' => 'http://twitter.com/thea_17forever',
                                                      'name' => 'thea ready set',
                                                      'nick' => 'thea_17forever',
                                                      'photo_url' => 'http://a0.twimg.com/profile_images/2938561205/24262ffff8aca5ea4a765c88c79a1056_normal.jpeg',
                                                      'topsy_author_url' => 'http://topsy.com/twitter/thea_17forever?utm_source=otter',
                                                      'influence_level' => 7
                                                    },
                                        'date_alpha' => '12 hours ago',
                                        'highlight' => 'i can&#39;t find any of the links!! http://t.co/XhPP829K WORK YOUR MAGIC '
                                      }
                                    ]
                        }
        };
```