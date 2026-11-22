from browser import Browser

browser = Browser()

print("=== PENGUJIAN BROWSER ===")

print("\n1. Pengujian Visit")
browser.visit("Google")
browser.visit("YouTube")
browser.visit("Facebook")

print("\n2. Pengujian Back")
browser.back()
browser.show_current_page()

print("\n3. Pengujian Forward")
browser.forward()
browser.show_current_page()

print("\n4. Pengujian Back Saat Kosong")
browser.back()
browser.back()
browser.back()

print("\n5. Pengujian Forward Saat Kosong")
browser.forward()

print("\n=== PENGUJIAN SELESAI ===")
