CREATE SCHEMA IF NOT EXISTS public;

CREATE TABLE IF NOT EXISTS public.users (
    id bigint GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id bigint NOT NULL UNIQUE,
    user_name text,
    zodiac text,
    user_summary text,
    frequency text,
    language text,
    natal jsonb,
    level text,
    birth_datetime_place text,
    created_at timestamp with time zone NOT NULL DEFAULT timezone('utc'::text, now())
);