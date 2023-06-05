SELECT
  activities.uuid,
  users.display_name,
  users.handle,
  activities.message,
  activities.expires_at,
  activities.reply_to_activity_uuid,
  activities.expires_at
FROM public.activities
INNER JOIN public.users ON users.uuid = activities.user_uuid 
WHERE 
  activities.uuid = %(uuid)s