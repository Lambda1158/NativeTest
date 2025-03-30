import { useFonts, Montserrat_400Regular, Montserrat_700Bold } from '@expo-google-fonts/montserrat';
import {
  Poppins_400Regular,
  Poppins_700Bold,
  Poppins_600SemiBold,
} from '@expo-google-fonts/poppins';
import { Text, View, ActivityIndicator } from 'react-native';
import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';

export default function Layout() {
  const [fontsLoaded] = useFonts({
    'Montserrat-Regular': Montserrat_400Regular,
    'Montserrat-Bold': Montserrat_700Bold,
    'Poppins-Regular': Poppins_400Regular,
    'Poppins-Bold': Poppins_700Bold,
    'Poppins-Semi': Poppins_600SemiBold,
  });
  if (!fontsLoaded)
    return (
      <View className="flex-1 items-center justify-center bg-spotify-black">
        <ActivityIndicator
          className="flex-1 items-center justify-center"
          size="large"
          color="#07301e"
        />
      </View>
    );
  return (
    <SafeAreaProvider>
      <StatusBar style="light" />
      <SafeAreaView className='flex-1'>
        <Stack>
          <Stack.Screen name="index" options={{ headerShown: false }} />
          <Stack.Screen name="(auth)" options={{ headerShown: false }} />
          <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
        </Stack>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}
