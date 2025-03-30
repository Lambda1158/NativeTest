import { Image, Text, TouchableOpacity, View } from 'react-native';
import { router } from 'expo-router';
import { useRef, useState } from 'react';
import Swiper from 'react-native-swiper';
import { itemsWelcome } from 'app/constant';
import CustomButton from '@/components/CustomeButton';
export default function welcome() {
  const swiperRef = useRef<Swiper>(null);
  const [activeIndex, setActiveIndex] = useState(0);
  const lastSlide = activeIndex === itemsWelcome?.length - 1;

  return (
    <View className=" h-full flex-1 items-center justify-center bg-spotify-black">
      <TouchableOpacity
        className="absolute right-0 top-0 p-5"
        onPress={() => router.replace('/(auth)/sign-in')}>
        <Text className="text-spotify-white font-mont text-base">Skip</Text>
      </TouchableOpacity>
      <View className="mt-20">
        <Text className="font-montbold text-4xl text-spotify-green">Bienvenido a Melody</Text>
      </View>
      <Swiper
        ref={swiperRef}
        loop={false}
        dot={<View className="mx-1 h-[6px] w-[36px] bg-spotify-green" />}
        activeDot={<View className="mx-1 h-[6px] w-[34px] bg-spotify-dark-green" />}
        onIndexChanged={(index) => setActiveIndex(index)}>
        {itemsWelcome.map((item) => (
          <View key={item.id} className="flex-1 items-center justify-center p-5">
            <Image
              className="h-[300px] w-full bg-transparent"
              resizeMode="contain"
              source={item.image}
            />
            <Text className="font-mont text-4xl text-spotify-white">{item.title}</Text>
            <Text className="mt-6 text-center text-xl italic text-spotify-white">
              {item.description}
            </Text>
          </View>
        ))}
      </Swiper>
      <CustomButton
        onPress={
          lastSlide ? () => router.replace('/(auth)/sign-in') : () => swiperRef.current?.scrollBy(1)
        }
        title={lastSlide ? 'Get Started' : 'Next'}
        className="mb-2"
      />
    </View>
  );
}
