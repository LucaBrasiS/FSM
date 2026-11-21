"""A1 gramer üniteleri: beş ünite, ünite başına zorluk sırasıyla 30 beş şıklı soru (10 temel, 10 orta, 10 ileri).
Her satır: (cümle, doğru cevap, dört yanlış şık, açıklama). Şıkların sırası sabit tohumla karıştırılır.
Kullanım: python3 gramer-a1-uret.py <çıktı.json>   (data/gramer-a1.json)"""
import json, random, sys

U = []

U.append(dict(id='a1-be', no=1, en='am / is / are', ad='Olmak fiili', kisa='I am, he is, they are; olumsuz, soru ve kısa cevaplar',
 notlar="""## Temel kural
- İngilizcede "-dir, -im, -sin" anlamını **am / is / are** verir.
- **I** ile **am**: *I am a student.*
- **he, she, it** ve tek bir kişi ya da şey ile **is**: *She is my sister.* *The book is new.*
- **you, we, they** ve birden çok kişi ya da şey ile **are**: *They are at school.* *The apples are red.*

## Olumsuz ve soru
- Olumsuz için arkasına **not** gelir: *He is not at home.* Kısası: *isn't, aren't*. (*I am not* kısalmaz, yalnız *I'm not* olur.)
- Soruda **am / is / are** başa geçer: *Are you tired?* *Is she your teacher?*

## Kısa cevaplar
- *Yes, I am.* *No, he isn't.* *Yes, they are.*
- Olumlu kısa cevapta kısaltma yapılmaz: *Yes, I am.* (*Yes, I'm.* olmaz.)""",
 items=[
 ("I ---- a student.", "am", ["is", "are", "be", "does"], "'I' ile her zaman 'am' kullanılır: I am a student."),
 ("She ---- my sister.", "is", ["am", "are", "be", "do"], "'She' tek kişidir, 'is' alır: She is my sister."),
 ("They ---- at school.", "are", ["is", "am", "be", "does"], "'They' çoğuldur, 'are' alır: They are at school."),
 ("He ---- a doctor.", "is", ["are", "am", "be", "have"], "'He' tek kişidir, 'is' alır."),
 ("We ---- friends.", "are", ["is", "am", "be", "has"], "'We' ile 'are' kullanılır: We are friends."),
 ("It ---- a cat.", "is", ["are", "am", "be", "do"], "'It' ile 'is' kullanılır: It is a cat."),
 ("You ---- very kind.", "are", ["is", "am", "be", "does"], "'You' tek kişiye de söylense 'are' alır: You are very kind."),
 ("My mother ---- a teacher.", "is", ["are", "am", "be", "have"], "'My mother' tek kişidir (she), bu yüzden 'is'."),
 ("The apples ---- red.", "are", ["is", "am", "be", "has"], "'The apples' çoğuldur (they), bu yüzden 'are'."),
 ("I ---- from Turkey.", "am", ["is", "are", "be", "do"], "'I' ile 'am': I am from Turkey."),
 ("He ---- not at home now.", "is", ["are", "am", "do", "does"], "Olumsuzda da kural aynı: he + is + not."),
 ("---- you tired?", "Are", ["Is", "Am", "Do", "Does"], "Soruda fiil başa geçer; 'you' ile 'are': Are you tired?"),
 ("---- she your teacher?", "Is", ["Are", "Am", "Do", "Does"], "'She' ile 'is'; soruda başa geçer: Is she your teacher?"),
 ("I ---- not hungry.", "am", ["is", "are", "do", "does"], "'I' ile 'am': I am not hungry."),
 ("They ---- not in the kitchen.", "are", ["is", "am", "do", "does"], "'They' ile 'are': They are not in the kitchen."),
 ("---- it cold today?", "Is", ["Are", "Am", "Do", "Does"], "'It' ile 'is': Is it cold today?"),
 ("We ---- not late.", "are", ["is", "am", "do", "does"], "'We' ile 'are': We are not late."),
 ("---- your parents at home?", "Are", ["Is", "Am", "Do", "Does"], "'Your parents' çoğuldur (they), bu yüzden 'Are'."),
 ("The book ---- not on the table.", "is", ["are", "am", "do", "have"], "'The book' tek bir şeydir (it), bu yüzden 'is'."),
 ("---- I in the right room?", "Am", ["Is", "Are", "Do", "Does"], "'I' ile soru da 'am' ile kurulur: Am I in the right room?"),
 ("\"Are you a student?\" \"Yes, I ----.\"", "am", ["is", "are", "do", "'m"], "Olumlu kısa cevapta kısaltma yapılmaz: Yes, I am."),
 ("\"Is he your brother?\" \"No, he ----.\"", "isn't", ["aren't", "am not", "doesn't", "not"], "'He' ile olumsuz kısa cevap: No, he isn't."),
 ("She ---- from Spain; she's from Italy.", "isn't", ["aren't", "am not", "don't", "not is"], "İkinci cümle İtalyalı olduğunu söylüyor, yani İspanyalı değil: she isn't."),
 ("My brother and I ---- in the same class.", "are", ["is", "am", "be", "does"], "'My brother and I' iki kişidir (we), bu yüzden 'are'."),
 ("\"Are they at the park?\" \"Yes, they ----.\"", "are", ["is", "am", "do", "does"], "Kısa cevapta sorudaki fiil tekrar edilir: Yes, they are."),
 ("This bag ---- very heavy.", "is", ["are", "am", "be", "have"], "'This bag' tek bir şeydir, 'is' alır."),
 ("The children ---- happy today.", "are", ["is", "am", "be", "has"], "'Children' çoğuldur (they), 'are' alır."),
 ("Where ---- your shoes?", "are", ["is", "am", "do", "does"], "'Shoes' çoğuldur: Where are your shoes?"),
 ("What ---- your name?", "is", ["are", "am", "do", "does"], "'Your name' tek bir şeydir: What is your name?"),
 ("How old ---- you?", "are", ["is", "am", "do", "have"], "Yaş 'be' fiiliyle sorulur ve 'you' ile 'are' gelir: How old are you?"),
 ]))

U.append(dict(id='a1-art', no=2, en='a / an and plurals', ad='a, an ve çoğullar', kisa='a book, an apple; cats, boxes, children',
 notlar="""## a mı, an mı?
- Tek bir şeyden söz ederken başına **a** ya da **an** gelir: *a book, a cat*.
- Kelime **sesli bir sesle** başlıyorsa **an** kullanılır: *an apple, an egg, an orange, an umbrella*.
- Önemli olan harf değil sestir: *an hour* (h okunmaz), *a university* ("yu" diye başlar).
- Araya sıfat girerse sıfatın ilk sesine bakılır: *an old car, a big apple*.

## Çoğullar
- Çoğu kelimeye **-s** eklenir: *cat → cats, book → books*.
- **-s, -x, -ch, -sh** ile bitenlere **-es**: *bus → buses, box → boxes, watch → watches*.
- Sessiz harf + **y** ile bitenlerde **-ies**: *baby → babies*.
- Bazıları kuralsızdır: *man → men, woman → women, child → children, person → people, foot → feet, tooth → teeth*.
- Çoğul kelimenin başına **a / an** gelmez: *two cats* (*a cats* olmaz).""",
 items=[
 ("I have ---- apple.", "an", ["a", "two", "many", "these"], "'Apple' sesli bir sesle başlar, bu yüzden 'an'."),
 ("She has ---- cat.", "a", ["an", "two", "many", "these"], "'Cat' sessiz bir sesle başlar, bu yüzden 'a'."),
 ("It is ---- egg.", "an", ["a", "two", "many", "those"], "'Egg' sesli bir sesle başlar: an egg."),
 ("He is ---- teacher.", "a", ["an", "two", "some", "these"], "Mesleklerden önce 'a / an' gelir; 'teacher' sessizle başlar: a teacher."),
 ("This is ---- orange.", "an", ["a", "two", "many", "these"], "'Orange' sesli bir sesle başlar: an orange."),
 ("I want ---- banana, please.", "a", ["an", "two", "many", "those"], "'Banana' sessizle başlar: a banana."),
 ("My father has ---- old car.", "an", ["a", "two", "many", "these"], "Araya sıfat girince sıfata bakılır; 'old' sesliyle başlar: an old car."),
 ("There is ---- book on the table.", "a", ["an", "two", "many", "these"], "'There is' tek bir şey anlatır; 'book' sessizle başlar: a book."),
 ("She is ---- English teacher.", "an", ["a", "two", "some", "those"], "'English' sesliyle başlar: an English teacher."),
 ("We have ---- big house.", "a", ["an", "two", "many", "these"], "'Big' sessizle başlar: a big house."),
 ("I have two ----.", "cats", ["cat", "a cat", "an cat", "cates"], "'Two' birden fazla demektir; çoğul için -s eklenir: cats."),
 ("There are three ---- on the table.", "books", ["book", "a book", "bookes", "an book"], "'Three' çoğul ister: books."),
 ("She has two ----.", "brothers", ["brother", "a brother", "brotheres", "an brother"], "'Two' çoğul ister: brothers."),
 ("We need four ----.", "boxes", ["box", "boxs", "a box", "boxies"], "-x ile biten kelimeler çoğulda -es alır: boxes."),
 ("I can see five ----.", "buses", ["bus", "buss", "a bus", "busies"], "-s ile biten kelimeler çoğulda -es alır: buses."),
 ("There are two ---- in the garden.", "children", ["child", "childs", "childrens", "a child"], "'Child' kuralsızdır; çoğulu 'children'."),
 ("He has three ----.", "watches", ["watch", "watchs", "a watch", "watchies"], "-ch ile biten kelimeler çoğulda -es alır: watches."),
 ("Two ---- are in the room.", "men", ["man", "mans", "mens", "a man"], "'Man' kuralsızdır; çoğulu 'men'."),
 ("Many ---- live in this city.", "people", ["person", "a person", "peoples", "a people"], "'Person' kelimesinin çoğulu 'people'."),
 ("Two ---- work in this shop.", "women", ["woman", "womans", "womens", "a woman"], "'Woman' kuralsızdır; çoğulu 'women'."),
 ("I eat ---- egg and two tomatoes for breakfast.", "an", ["a", "two", "many", "these"], "'Egg' tekil ve sesliyle başlıyor: an egg."),
 ("The ---- are in the kitchen.", "glasses", ["glass", "glasss", "a glass", "glassies"], "'Are' çoğul ister; -ss ile biten kelime -es alır: glasses."),
 ("My ---- hurt after the long walk.", "feet", ["foot", "foots", "feets", "a foot"], "'Foot' kuralsızdır; çoğulu 'feet'."),
 ("She brushes her ---- every morning.", "teeth", ["tooth", "tooths", "teeths", "a tooth"], "'Tooth' kuralsızdır; çoğulu 'teeth'."),
 ("It is ---- umbrella.", "an", ["a", "two", "many", "these"], "'Umbrella' sesli bir sesle başlar: an umbrella."),
 ("He works in ---- hospital.", "a", ["an", "two", "many", "these"], "'Hospital' kelimesinde h okunur, yani sessizle başlar: a hospital."),
 ("I wait for ---- hour every day.", "an", ["a", "two", "many", "these"], "'Hour' kelimesinde h okunmaz; sesli bir sesle başlar: an hour."),
 ("She studies at ---- university.", "a", ["an", "two", "many", "these"], "'University' \"yu\" sesiyle başlar; bu sessiz bir sestir: a university."),
 ("There are six ---- in the park.", "babies", ["baby", "babys", "a baby", "babyes"], "Sessiz harf + y ile biten kelimede y düşer, -ies gelir: babies."),
 ("Three ---- are on the plate.", "sandwiches", ["sandwich", "sandwichs", "a sandwich", "sandwichies"], "-ch ile biten kelimeler çoğulda -es alır: sandwiches."),
 ]))

U.append(dict(id='a1-this', no=3, en='this / that, my / your', ad='Bu, şu ve benim, senin', kisa='this, that, these, those; my, your, his, her, our, their',
 notlar="""## this, that, these, those
- Yakındaki tek şey için **this**: *This is my pen.*
- Yakındaki birden çok şey için **these**: *These are my shoes.*
- Uzaktaki tek şey için **that**: *That is a plane.*
- Uzaktaki birden çok şey için **those**: *Those are my friends.*
- İpucu: *here* yakını, *over there* uzağı gösterir. Fiil *is* ise tekil, *are* ise çoğul gerekir.

## my, your, his, her...
- Bir şeyin kime ait olduğunu söylerler ve hep bir ismin önünde dururlar: *my book, your name*.
- *I → my, you → your, he → his, she → her, it → its, we → our, they → their*.
- *His* erkek, *her* kadın içindir: *He is Can. His sister is Elif.* *She is Elif. Her brother is Can.*""",
 items=[
 ("---- is my pen here.", "This", ["These", "Those", "They", "We"], "'Here' yakını gösterir, 'is' tekildir: This."),
 ("---- are my shoes here.", "These", ["This", "That", "It", "He"], "Yakında ve çoğul ('are'): These."),
 ("Look! ---- is a plane in the sky over there.", "That", ["These", "Those", "They", "We"], "'Over there' uzağı gösterir, 'is' tekildir: That."),
 ("---- are my friends over there, near the door.", "Those", ["This", "That", "It", "She"], "Uzakta ve çoğul ('are'): Those."),
 ("---- apple here is very sweet.", "This", ["These", "Those", "They", "We"], "Yakında tek bir elma: This apple."),
 ("---- apples here are red.", "These", ["This", "That", "It", "He"], "Yakında birden çok elma: These apples."),
 ("Who is ---- man over there?", "that", ["these", "those", "they", "we"], "Uzakta tek bir kişi: that man."),
 ("Are ---- your keys over there on the table?", "those", ["this", "that", "it", "he"], "Uzakta ve çoğul ('keys'): those."),
 ("---- is my mother here next to me.", "This", ["These", "Those", "They", "We"], "Yanımdaki tek kişi: This is my mother."),
 ("---- are my parents here in the photo.", "These", ["This", "That", "It", "She"], "Yakında ve çoğul ('are'): These."),
 ("I have a sister. ---- name is Elif.", "Her", ["She", "His", "Their", "Hers"], "Kız kardeşe ait olan için 'her': Her name."),
 ("He is my brother. ---- name is Can.", "His", ["He", "Her", "Their", "Him"], "Erkeğe ait olan için 'his': His name."),
 ("I am Ali. ---- surname is Kaya.", "My", ["I", "Me", "Your", "Mine"], "'I' için iyelik sözü 'my': My surname."),
 ("We live here. This is ---- house.", "our", ["we", "us", "ours", "I"], "'We' için iyelik sözü 'our': our house."),
 ("They have a dog. ---- dog is very big.", "Their", ["They", "Them", "Theirs", "There"], "'They' için iyelik sözü 'their': Their dog."),
 ("\"What is ---- name?\" \"I'm Deniz.\"", "your", ["you", "yours", "we", "they"], "Karşıdakinin adını sorarken 'your': What is your name?"),
 ("This is my friend Ayşe and this is ---- brother.", "her", ["she", "hers", "they", "we"], "Ayşe'ye ait olan için 'her': her brother."),
 ("I love ---- mother very much.", "my", ["I", "me", "mine", "we"], "İsmin önünde 'my' durur: my mother."),
 ("Mr and Mrs Demir are teachers. ---- school is near here.", "Their", ["They", "Them", "Theirs", "There"], "İki kişiye ait olan için 'their': Their school."),
 ("You are late. Where is ---- homework?", "your", ["you", "yours", "they", "we"], "'You' için iyelik sözü 'your': your homework."),
 ("\"Is ---- your bag here?\" \"Yes, it is.\"", "this", ["these", "those", "they", "we"], "Yakında tek bir çanta ('is'): this."),
 ("\"Are ---- your books over there?\" \"Yes, they are.\"", "those", ["this", "that", "it", "he"], "Uzakta ve çoğul ('are', 'books'): those."),
 ("---- shoes over there are very expensive.", "Those", ["This", "That", "It", "She"], "Uzakta ve çoğul ('shoes'): Those shoes."),
 ("My sister has a new phone. ---- phone is blue.", "Her", ["She", "Hers", "His", "He"], "Kız kardeşe ait olan için 'her': Her phone."),
 ("The children are in the garden with ---- friends.", "their", ["they", "them", "theirs", "there"], "'The children' (they) için 'their': their friends."),
 ("Can and I are brothers. ---- father is a doctor.", "Our", ["We", "Us", "Ours", "I"], "'Can and I' biziz (we); iyelik sözü 'our'."),
 ("---- is my grandfather in that old photo over there.", "That", ["These", "Those", "They", "We"], "Uzakta tek bir kişi ('is'): That."),
 ("I can't find ---- keys. Are they in the kitchen?", "my", ["I", "me", "mine", "we"], "İsmin önünde 'my' durur: my keys."),
 ("---- flowers here in my hand are for you.", "These", ["This", "That", "It", "He"], "Yakında ve çoğul ('flowers', 'are'): These."),
 ("Elif, is this ---- pencil?", "your", ["you", "yours", "they", "we"], "Karşıdakine ait olan için 'your': your pencil."),
 ]))

U.append(dict(id='a1-can', no=4, en='can / can\'t', ad='Yapabilmek', kisa='I can swim, she can\'t drive; Can you...? Yes, I can.',
 notlar="""## Temel kural
- **can** "-ebilmek" demektir; yapabildiğimiz şeyleri anlatır: *I can swim.*
- Olumsuzu **can't** (cannot): *She can't drive.*
- **can** herkes için aynıdır, sonuna -s gelmez: *He can swim.* (*He cans* olmaz.)
- **can**'den sonra fiil yalın gelir: *She can speak English.* (*can speaks, can to speak, can speaking* olmaz.)

## Soru ve kısa cevap
- Soruda **can** başa geçer: *Can you swim?*
- Kısa cevap: *Yes, I can.* *No, I can't.*
- Rica ederken de kullanılır: *Can I use your pen?* *Can you open the window, please?*""",
 items=[
 ("I ---- swim.", "can", ["cans", "am", "is", "to can"], "Yapabildiğimiz şey için 'can' ve yalın fiil: I can swim."),
 ("She ---- speak English.", "can", ["cans", "is", "are", "does can"], "'Can' herkes için aynıdır, -s almaz: She can speak."),
 ("Birds ---- fly.", "can", ["cans", "is", "am", "does"], "Kuşlar uçabilir: Birds can fly."),
 ("Fish live in water. They ---- walk.", "can't", ["can", "cans", "isn't", "don't can"], "Balıklar yürüyemez; olumsuz için 'can't'."),
 ("He can ---- the guitar.", "play", ["plays", "playing", "to play", "played"], "'Can'den sonra fiil yalın gelir: can play."),
 ("We can ---- you.", "help", ["helps", "helping", "to help", "helped"], "'Can'den sonra fiil yalın gelir: can help."),
 ("---- you swim?", "Can", ["Are", "Is", "Do can", "Cans"], "Soruda 'can' başa geçer: Can you swim?"),
 ("My baby sister is one year old. She ---- read.", "can't", ["can", "cans", "isn't", "aren't"], "Bir yaşındaki bebek okuyamaz: She can't read."),
 ("I can ---- a bike.", "ride", ["rides", "riding", "to ride", "rode"], "'Can'den sonra fiil yalın gelir: can ride."),
 ("Dogs ---- run fast.", "can", ["cans", "is", "am", "does"], "Köpekler hızlı koşabilir: Dogs can run fast."),
 ("\"Can you cook?\" \"Yes, I ----.\"", "can", ["can't", "am", "do", "cook"], "Olumlu kısa cevap: Yes, I can."),
 ("\"Can he drive?\" \"No, he ----.\"", "can't", ["can", "isn't", "doesn't", "not"], "Olumsuz kısa cevap: No, he can't."),
 ("She can ---- three languages.", "speak", ["speaks", "speaking", "to speak", "spoke"], "'Can'den sonra fiil yalın gelir: can speak."),
 ("---- your brother play football?", "Can", ["Is", "Are", "Cans", "Do can"], "Soruda 'can' başa geçer: Can your brother play football?"),
 ("I ---- hear you. Please speak up.", "can't", ["can", "am not", "isn't", "don't can"], "Daha yüksek sesle konuşmasını istiyor, yani duyamıyor: I can't hear you."),
 ("They can ---- very well.", "dance", ["dances", "dancing", "to dance", "danced"], "'Can'den sonra fiil yalın gelir: can dance."),
 ("Can I ---- your pen, please?", "use", ["uses", "using", "to use", "used"], "Rica cümlesinde de 'can'den sonra yalın fiil: Can I use...?"),
 ("\"Can they come to the party?\" \"Yes, they ----.\"", "can", ["can't", "are", "do", "come"], "Olumlu kısa cevap: Yes, they can."),
 ("He ---- come today because he is sick.", "can't", ["can", "cans", "isn't", "aren't"], "Hasta olduğu için gelemiyor: He can't come."),
 ("What can you ---- in the picture?", "see", ["sees", "seeing", "to see", "saw"], "Soruda da 'can'den sonra yalın fiil: can you see."),
 ("Can you ---- the window, please? It's hot.", "open", ["opens", "opening", "to open", "opened"], "Rica cümlesi: Can you open...? Fiil yalın gelir."),
 ("My grandfather is 90, but he ---- still ride a bike.", "can", ["can't", "cans", "is", "does"], "'But' beklenmeyen bir şey söyler: 90 yaşında ama hâlâ binebiliyor: he can."),
 ("I'm sorry, I ---- help you now. I'm very busy.", "can't", ["can", "cans", "am", "do"], "Özür diliyor ve meşgul, yani yardım edemiyor: I can't help."),
 ("---- she sing well?", "Can", ["Is", "Does can", "Cans", "Are"], "Soruda 'can' başa geçer: Can she sing well?"),
 ("We ---- see the sea from our window. It's beautiful.", "can", ["cans", "are", "is", "can't"], "Güzel olduğunu söylüyor, yani görebiliyorlar: We can see the sea."),
 ("\"Can I sit here?\" \"Yes, you ----.\"", "can", ["can't", "are", "do", "sit"], "İzin verirken: Yes, you can."),
 ("A cat can ---- a tree.", "climb", ["climbs", "climbing", "to climb", "climbed"], "'Can'den sonra fiil yalın gelir: can climb."),
 ("It's very dark. I ---- see anything.", "can't", ["can", "cans", "am not", "isn't"], "Karanlıkta hiçbir şey göremiyor: I can't see anything."),
 ("Where can I ---- a ticket?", "buy", ["buys", "buying", "to buy", "bought"], "Soruda da 'can'den sonra yalın fiil: can I buy."),
 ("She can play the piano, but she ---- play the guitar.", "can't", ["can", "cans", "isn't", "doesn't"], "'But' zıtlık bildirir: piyano çalabiliyor ama gitar çalamıyor."),
 ]))

U.append(dict(id='a1-pres', no=5, en='I like / she likes', ad='Geniş zamanın temelleri', kisa='I work, he works; don\'t / doesn\'t; Do you...? Does she...?',
 notlar="""## Temel kural
- Her zaman yaptığımız şeyleri ve alışkanlıkları anlatırken fiil yalın kullanılır: *I drink tea every morning.*
- **he, she, it** ile fiile **-s** eklenir: *She likes coffee.* *He works in a bank.*
- **-s, -sh, -ch, -x, -o** ile biten fiiller **-es** alır: *watches, brushes, goes*.
- Sessiz harf + **y** ile biten fiilde **-ies**: *study → studies*.
- *have* fiili *he, she, it* ile **has** olur: *Ali has two brothers.*

## Olumsuz
- **I, you, we, they** ile **don't**: *I don't like fish.*
- **he, she, it** ile **doesn't**: *She doesn't like milk.*
- *don't / doesn't*'tan sonra fiil yalın gelir: *She doesn't eat meat.* (*doesn't eats* olmaz.)

## Soru
- **I, you, we, they** ile **Do**: *Do you like pizza?*
- **he, she, it** ile **Does**: *Does he play tennis?*
- Kısa cevap: *Yes, I do.* *No, she doesn't.*""",
 items=[
 ("I ---- tea every morning.", "drink", ["drinks", "drinking", "am drink", "to drink"], "'I' ile fiil yalın kullanılır: I drink."),
 ("She ---- coffee.", "likes", ["like", "liking", "is like", "to like"], "'She' ile fiile -s eklenir: She likes."),
 ("He ---- in a bank.", "works", ["work", "working", "is work", "to work"], "'He' ile fiile -s eklenir: He works."),
 ("We ---- in Ankara.", "live", ["lives", "living", "are live", "to live"], "'We' ile fiil yalın kullanılır: We live."),
 ("They ---- football on Sundays.", "play", ["plays", "playing", "are play", "to play"], "'They' ile fiil yalın kullanılır: They play."),
 ("My mother ---- dinner every evening.", "cooks", ["cook", "cooking", "is cook", "to cook"], "'My mother' tek kişidir (she); fiil -s alır: cooks."),
 ("You ---- English very well.", "speak", ["speaks", "speaking", "are speak", "to speak"], "'You' ile fiil yalın kullanılır: You speak."),
 ("The cat ---- on the sofa.", "sleeps", ["sleep", "sleeping", "is sleep", "to sleep"], "'The cat' tek bir hayvandır (it); fiil -s alır: sleeps."),
 ("I ---- to school by bus.", "go", ["goes", "going", "am go", "to go"], "'I' ile fiil yalın kullanılır: I go."),
 ("My brother ---- TV in the evening.", "watches", ["watch", "watching", "is watch", "watchs"], "'My brother' (he) ile -ch ile biten fiil -es alır: watches."),
 ("I ---- like fish.", "don't", ["doesn't", "isn't", "am not", "not"], "'I' ile olumsuz 'don't': I don't like."),
 ("She ---- like milk.", "doesn't", ["don't", "isn't", "aren't", "not"], "'She' ile olumsuz 'doesn't': She doesn't like."),
 ("---- you like pizza?", "Do", ["Does", "Are", "Is", "Am"], "'You' ile soru 'Do' ile kurulur: Do you like...?"),
 ("---- he play tennis?", "Does", ["Do", "Is", "Are", "Am"], "'He' ile soru 'Does' ile kurulur: Does he play...?"),
 ("We ---- work on Sundays.", "don't", ["doesn't", "aren't", "isn't", "not"], "'We' ile olumsuz 'don't': We don't work."),
 ("My father ---- drink coffee.", "doesn't", ["don't", "isn't", "aren't", "not"], "'My father' (he) ile olumsuz 'doesn't'."),
 ("---- they live near here?", "Do", ["Does", "Are", "Is", "Am"], "'They' ile soru 'Do' ile kurulur."),
 ("---- your sister speak English?", "Does", ["Do", "Is", "Are", "Am"], "'Your sister' (she) ile soru 'Does' ile kurulur."),
 ("She doesn't ---- meat.", "eat", ["eats", "eating", "to eat", "ate"], "'Doesn't'tan sonra fiil yalın gelir: doesn't eat."),
 ("Do you ---- a car?", "have", ["has", "having", "to have", "had"], "'Do' ile kurulan soruda fiil yalın gelir: Do you have...?"),
 ("\"Do you like tea?\" \"Yes, I ----.\"", "do", ["does", "am", "like", "don't"], "Olumlu kısa cevap: Yes, I do."),
 ("\"Does she work here?\" \"No, she ----.\"", "doesn't", ["don't", "isn't", "not", "does"], "Olumsuz kısa cevap: No, she doesn't."),
 ("He ---- to work by train every day.", "goes", ["go", "going", "is go", "gos"], "'He' ile 'go' fiili -es alır: goes."),
 ("My sister ---- English at university.", "studies", ["study", "studys", "studying", "is study"], "Sessiz harf + y ile biten fiilde y düşer, -ies gelir: studies."),
 ("What time ---- the film start?", "does", ["do", "is", "are", "am"], "'The film' tek bir şeydir (it); soru 'does' ile kurulur."),
 ("Where ---- you live?", "do", ["does", "are", "is", "am"], "'You' ile soru 'do' ile kurulur: Where do you live?"),
 ("Ali ---- two brothers and a sister.", "has", ["have", "haves", "having", "is have"], "'Have' fiili 'he, she, it' ile 'has' olur: Ali has."),
 ("They ---- eat meat. They are vegetarians.", "don't", ["doesn't", "aren't", "isn't", "not"], "Vejetaryen oldukları için et yemezler; 'they' ile 'don't'."),
 ("My parents ---- in a hospital. They are doctors.", "work", ["works", "working", "are work", "to work"], "'My parents' çoğuldur (they); fiil yalın kullanılır: work."),
 ("She ---- her teeth every night.", "brushes", ["brush", "brushs", "brushing", "is brush"], "-sh ile biten fiil 'she' ile -es alır: brushes."),
 ]))

rnd = random.Random(1101)
out = {"t": [], "q": {}}
for u in U:
    assert len(u["items"]) == 30, (u["id"], len(u["items"]))
    rows = []
    for k, (q, right, wrong, why) in enumerate(u["items"]):
        opts = [right] + wrong
        assert len(set(opts)) == 5 and "----" in q, (u["id"], q)
        rnd.shuffle(opts)
        rows.append([q, opts, opts.index(right), why, "bosluk"])
    out["t"].append({"id": u["id"], "grp": "a", "no": u["no"], "en": u["en"], "ad": u["ad"], "kisa": u["kisa"], "not": u["notlar"]})
    out["q"][u["id"]] = rows
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print(len(U), "ünite", sum(len(v) for v in out["q"].values()), "soru")
