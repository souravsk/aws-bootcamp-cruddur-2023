-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Sourav Kumar','souravk326@gmail.com' , 'sourav_sovu_' ,'MOCK'),
  ('Sonu','souravk326+sonu@gmail.com' , 'sonu' ,'MOCK'),
  ('Son Goku','songoku02010@gmail.com' , 'goku' ,'MOCK'),
  ('Londo Mollari','lmollari@centari.com' ,'londo' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'sovu' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )