import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';
import { Text, View } from 'react-native';

export default function Home() {
  return (
    <SafeAreaProvider>
      <SafeAreaView className="flex-1 bg-gray-400">
        <View className="flex-1 items-center justify-center">
          <Text className="text-xl font-bold text-blue-600">
            ¡Hola, SafeArea No funciona tailwind !
          </Text>
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}
