import { View, Text } from 'react-native';

export default function Topbar() {
  return (
    <View className="flex-1 justify-between">
      <Text className="text-spotify-dark-green">Item 1</Text>
      <Text className="text-spotify-red">Item 2</Text>
      <Text className="text-spotify-green">Item 3</Text>
    </View>
  );
}
