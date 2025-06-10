def verifica_email(email):
    if '@' in email and '.com' in email:
        return 'email válido'
    else:
        return 'email incorreto'

def test_verifica_email():
    assert verifica_email('calabreso@gmail.com') == 'email válido'
    assert verifica_email('cuzinhoarroba.com') == 'email incorreto'