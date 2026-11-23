# RixMusic 0.3.0

کتابخانه کمکی و ماژولار برای ساخت ابزارهای موسیقی روبیکا با Rubpy. تمام فایل‌ها در ریشه پروژه هستند و هیچ پوشه داخلی در ZIP وجود ندارد.

## نصب

```bash
pip install -U rubpy
```

فایل‌های ZIP را در یک پوشه استخراج کنید و در همان پوشه اجرا کنید:

```bash
python -c "import rixmusic; print(rixmusic.__version__)"
```

## شروع سریع

```python
from rubpy import Client
from rixmusic import RixMusic, Track

async with Client(name="my_session") as client:
    music = RixMusic(client, owner_ids=["OWNER_GUID"])
    await music.add(
        "GROUP_GUID",
        Track("Song", "https://example.com/song.mp3")
    )
    track = await music.next("GROUP_GUID")
    print(track)
```

## امکانات موجود

- صف موسیقی: add, next/skip, clear, shuffle, remove, peek
- دانلود مستقیم URLهای HTTP/HTTPS با محدودیت حجم
- مدیریت مالک و ادمین در حافظه
- ارسال فایل موسیقی، ویدئو، ویس و ویدئوی گرد با متدهای Rubpy
- ایجاد گفت‌وگوی صوتی گروه با `create_group_voice_chat`
- تلاش برای پخش فایل در گفت‌وگوی صوتی از مسیر `voice_chat_player` با بررسی نتیجه واقعی
- خطاهای روشن برای متدهای پشتیبانی‌نشده

## محدودیت‌های مهم

1. **تماس صوتی/تصویری اکانت‌به‌اکانت:** در API مستندشده Rubpy متد تأییدشده‌ای برای شروع تماس مستقیم با یک کاربر پیدا نشده است. متدهای `call_account` و `video_call_account` عمداً `UnsupportedFeature` می‌دهند و تماس جعلی اعلام نمی‌کنند.
2. **تولید ویدئو:** این کتابخانه فایل ویدئویی موجود را ارسال می‌کند؛ موتور تولید ویدئو نیست.
3. **پخش در گفت‌وگوی صوتی:** ساخت ویس‌چت به‌تنهایی پخش نیست. پخش به RTC و وابستگی‌های سازگار Rubpy مانند aiortc/PyAV نیاز دارد. روی بعضی نسخه‌های Android/Pydroid ممکن است نصب یا اجرا ممکن نباشد.
4. **جست‌وجوی آهنگ:** دانلودر فقط لینک مستقیم فایل را می‌گیرد؛ سرویس جست‌وجوی آهنگ یا دور زدن محدودیت سرویس‌ها ارائه نمی‌کند.
5. مدیریت دسترسی این نسخه در حافظه است؛ برای ماندگاری بعد از خاموش‌شدن برنامه باید ذخیره‌سازی اضافه شود.

## ساختار

همه فایل‌ها کنار هم هستند:

- `rixmusic.py` رابط اصلی
- `rixmusic_core.py` کلاس اصلی
- `rixmusic_rubpy.py` اتصال Rubpy
- `rixmusic_voice.py` گفت‌وگوی صوتی
- `rixmusic_media.py` ارسال رسانه
- `rixmusic_queue.py` صف
- `rixmusic_models.py` مدل‌ها
- `rixmusic_permissions.py` دسترسی‌ها
- `rixmusic_downloader.py` دانلودر
- `rixmusic_errors.py` خطاها
- `example_bot.py` نمونه
- `pyproject.toml` مشخصات پروژه

## مجوز

MIT
