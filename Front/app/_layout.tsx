import { View, Text } from 'react-native';
import { Stack, Slot } from 'expo-router';
export default function Layout() {
  return (
    <View className="flex-1">
      <Text className="mx-auto mt-20">Este es el layout</Text>
      <Stack />
    </View>
  );
}
