import { useFonts, Montserrat_400Regular, Montserrat_700Bold } from '@expo-google-fonts/montserrat';
import { Poppins_400Regular,Poppins_700Bold, Poppins_600SemiBold } from '@expo-google-fonts/poppins';
import { Text, View } from 'react-native';
import { Stack } from 'expo-router';

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
      <View>
        <Text>Cargando fuentes</Text>
      </View>
    );
  return (
    <Stack>
      <Stack.Screen name="index" options={{ headerShown: false }} />
      <Stack.Screen name="(auth)" options={{ headerShown: false }} />
      <Stack.Screen name="(tabs)" options={{ headerShown: false }} />
    </Stack>
  );
}
