import { Tabs } from 'expo-router';
import Entypo from '@expo/vector-icons/Entypo';
import FontAwesome from '@expo/vector-icons/FontAwesome';

export default function TabsLayout() {
  return (
    <Tabs>
      <Tabs.Screen
        name="charts"
        options={{
          title: 'Charts',
          headerShown: false,
          tabBarIcon: () => <Entypo name="pie-chart" size={24} color="black" />,
        }}
      />
      <Tabs.Screen
        name="music"
        options={{
          title: 'Music',
          headerShown: false,
          tabBarIcon: () => <FontAwesome name="music" size={24} color="black" />,
        }}
      />
    </Tabs>
  );
}
