import { Text, View, ScrollView, Button, Pressable } from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Link } from 'expo-router';

export default function Home() {
  const insets = useSafeAreaInsets();
  return (
    <View className="flex-1 items-center justify-center bg-black ">
      <Text className="text-2xl font-bold text-spotify-green">
        Esta es una app de Spotify Wrapped
      </Text>
      <Pressable
        onPress={() => alert('Hola')}
        className=" mx-auto mt-10 w-24 rounded-sm bg-spotify-white p-2">
        <Text className="text-center text-lg text-spotify-green">Refresh!!</Text>
      </Pressable>
      <Link href={'/charts'} asChild>
        <Pressable className="rounded-lg bg-spotify-black p-2">
          <Text className=" text-2xl text-spotify-green">Take me to charts</Text>
        </Pressable>
      </Link>
    </View>
  );
}
