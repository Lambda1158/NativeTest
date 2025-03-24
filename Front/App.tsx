import './global.css';
import '@expo/metro-runtime';
import Home from 'app/components/home';
import { StatusBar } from 'expo-status-bar';
import { SafeAreaProvider } from 'react-native-safe-area-context';

export default function App() {
  return (
    <SafeAreaProvider>
        <StatusBar style="light" />
        <Home />
    </SafeAreaProvider>
  );
}
