import { SafeAreaProvider, SafeAreaView } from 'react-native-safe-area-context';
import { Text, View } from 'react-native';

export default function App() {
  return (
    <SafeAreaProvider>
      <SafeAreaView className="flex-1 bg-gray-100">
        <View className="flex-1 items-center justify-center">
          <Text className="text-xl font-bold text-blue-600">¡Hola, SafeArea con NativeWind!</Text>
        </View>
      </SafeAreaView>
    </SafeAreaProvider>
  );
}
