import { View, Text } from 'react-native';
import CustomButton from '@/components/CustomeButton';
import { router } from 'expo-router';
import { useAuthRequest, makeRedirectUri } from 'expo-auth-session';
import { PROXY } from '@/constant';
import { CLIENT_ID } from '@env';

export default function Signin() {
  const [request, response, promptAsync] = useAuthRequest(
    {
      clientId: CLIENT_ID,
      redirectUri: makeRedirectUri({
        scheme: 'melody',
        path: 'auth-callback', // Ruta ficticia en Expo
      }),
      scopes: ['user-read-email'],
    },
    {
      authorizationEndpoint: PROXY, // Tu endpoint Flask
    }
  );
  return (
    <View className="flex-1 items-center justify-center bg-spotify-black">
      <Text className="font-montbold text-4xl text-spotify-green ">Sign in</Text>
      <CustomButton onPress={() => promptAsync()} title="Sing up With Spotify!"></CustomButton>
    </View>
  );
}
