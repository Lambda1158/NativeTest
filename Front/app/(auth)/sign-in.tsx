import { SafeAreaView } from 'react-native-safe-area-context';
import { Text } from 'react-native';
import CustomButton from '@/components/CustomeButton';
import { router } from 'expo-router';
export default function Signin() {
  return (
    <SafeAreaView className="flex-1 items-center justify-center bg-spotify-black">
      <Text className="font-montbold text-4xl text-spotify-green ">Sign in</Text>
      <CustomButton
        onPress={() => router.replace('/(auth)/welcome')}
        title="Volver al welcome"></CustomButton>
    </SafeAreaView>
  );
}
