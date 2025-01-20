// Helper function to get player image
export const getPlayerImage = (photoUrl) => {
  if (photoUrl) {
    return 'http://localhost:8000' + photoUrl;
  }
  return '/src/assets/images/defaultPlayer.png';
};

export const getAge = (dateString) => {
    if (!dateString) {
        return null;
    }
    const today = new Date();
    const birthDate = new Date(dateString);
    let age = today.getFullYear() - birthDate.getFullYear();
    const month = today.getMonth() - birthDate.getMonth();
    if (month < 0 || (month === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    return age;
}