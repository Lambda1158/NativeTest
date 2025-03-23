import { Stack } from 'expo-router';
import { View } from 'react-native';
export default function Layout() {
  return (
    <View className='flex-1 '>
      <Stack
        screenOptions={{
          headerStyle: {
            backgroundColor: 'black', 
          },
          headerTintColor: '#fff', 
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}/>
    </View>
  );
}
