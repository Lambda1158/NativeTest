import { SafeAreaView } from 'react-native-safe-area-context';
import { Image, Text, TouchableOpacity, View } from 'react-native';
import { Link, router } from 'expo-router';
import { useRef, useState } from 'react';
import Swiper from 'react-native-swiper';
import { itemsWelcome } from 'app/constant';
export default function welcome() {
  const swiperRef = useRef<Swiper>(null);
  const [activeIndex, setActiveIndex] = useState(0);

  return (
    <SafeAreaView className="h-full flex-1 items-center justify-center bg-spotify-black">
      <TouchableOpacity
        className=" mr-0 p-5"
        onPress={() => router.replace('/(auth)/sign-in')}>
        <Text className="text-spotify-white">Skip</Text>
      </TouchableOpacity>
      <View className="">
        <Text className="text-2xl font-bold text-spotify-green">
          Esta es una app de Spotify Wrapped
        </Text>
      </View>
      <Swiper
        ref={swiperRef}
        loop={false}
        dot={<View className="mx-1 h-[4px] w-[32px] bg-spotify-green" />}
        activeDot={<View className="mx-1 h-[4px] w-[32px] bg-spotify-dark-green" />}
        onIndexChanged={(index) => setActiveIndex(index)}>
        {itemsWelcome.map((item) => (
          <View key={item.id} className='flex-1 justify-center items-center p-5'>
            <Text className='text-spotify-white text-2xl font-bold'>{item.title}</Text>
			<Image className='w-full h-[300px] bg-transparent' resizeMode='contain' source={item.image}></Image>
			<Text className='text-spotify-white text-lg'>{item.description}</Text>
          </View>
        ))}
      </Swiper>
    </SafeAreaView>
  );
}
