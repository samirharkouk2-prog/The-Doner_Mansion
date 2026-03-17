import codecs
import re
import os

file_path = "c:\\Users\\E14\\Downloads\\Nouveau dossier (9)\\index.html"
with codecs.open(file_path, 'r', 'utf-8') as f:
    html = f.read()

# Replace <title>
html = html.replace("<title>The Wall Snack & Resto</title>", "<title>The Döner Mansion</title>")

# Replace logo alt (multiple places)
html = html.replace('alt="The Wall Snack & Resto Logo"', 'alt="The Döner Mansion Logo"')
html = html.replace('alt="The Wall Snack & Resto"', 'alt="The Döner Mansion"')

# Hero section replace
old_hero = """        <p class="punchline">Street Food Moderne</p>
        <h1>THE WALL SNACK & RESTO</h1>
        <p>Le spot urbain pour burgers, tacos, pizzas et bien plus. Rapide, généreux, et fait pour commander facilement.</p>
        <div class="hero-btns">
            <a href="#menu" class="btn-order">Voir le menu</a>
            <a href="https://wa.me/213555219684" target="_blank" class="btn-outline">Commander WhatsApp</a>
        </div>"""
new_hero = """        <p class="punchline">Modern Fast Food Concept</p>
        <h1>THE DÖNER MANSION</h1>
        <p>A modern street food concept serving Berlin-style Döner, New York platters, Nashville wings and premium smashed burgers for dine-in, takeaway, and delivery.</p>
        <div class="hero-btns">
            <a href="#menu" class="btn-order">Voir le menu</a>
            <a href="https://wa.me/213796663395" target="_blank" class="btn-outline">Commander WhatsApp</a>
        </div>"""
html = html.replace(old_hero, new_hero)

old_info_grid = """            <div class="info-card reveal">
                <h4>Localisation</h4>
                <p style="color: var(--light-gray);">Dely Ibrahim, Alger</p>
            </div>
            <div class="info-card reveal">
                <h4>Commander</h4>
                <p style="color: var(--light-gray);">Téléphone : 0555 21 96 84</p>
            </div>"""
new_info_grid = """            <div class="info-card reveal">
                <h4>Localisation</h4>
                <p style="color: var(--light-gray);">Algeria & Sweden</p>
            </div>
            <div class="info-card reveal">
                <h4>Commander / Delivery</h4>
                <p style="color: var(--light-gray);">Tél : 07 96 66 33 95</p>
            </div>"""
html = html.replace(old_info_grid, new_info_grid)

# Highlights replace
old_highlights = """            <h2>Meilleures ventes</h2>
            <p style="color: var(--light-gray); margin-top: 15px;">Les incontournables du moment.</p>
        </div>
        <div class="menu-grid">
            <div class="menu-card reveal">
                <div class="card-content">
                    <p class="card-title">Smash</p>
                    <p class="card-desc">Cornichons, 50gr viande hachée, fromage, sauce smash.</p>
                    <div class="card-footer">
                        <p class="card-price">350 DZD</p>
                    </div>
                </div>
            </div>
            <div class="menu-card reveal">
                <div class="card-content">
                    <p class="card-title">Croustyl</p>
                    <p class="card-desc">Salade, tomate, 100gr poulet pané, fromage, sauce à l’ail.</p>
                    <div class="card-footer">
                        <p class="card-price">450 DZD</p>
                    </div>
                </div>
            </div>
            <div class="menu-card reveal">
                <div class="card-content">
                    <p class="card-title">Mixte</p>
                    <p class="card-desc">Steak haché, poulet pané, double fromage, sauce à l’ail.</p>
                    <div class="card-footer">
                        <p class="card-price">700 DZD</p>
                    </div>
                </div>
            </div>
        </div>"""
new_highlights = """            <h2>Spécialités</h2>
            <p style="color: var(--light-gray); margin-top: 15px;">Discover our signature dishes inspired by international street food.</p>
        </div>
        <div class="menu-grid">
            <div class="menu-card reveal">
                <div class="card-content">
                    <p class="card-title">Döner Classic</p>
                    <p class="card-desc">180g döner, sautéed vegetables (Berlin style), mozzarella with herbs, special sauces.</p>
                    <div class="card-footer">
                        <p class="card-price">800 DA</p>
                    </div>
                </div>
            </div>
            <div class="menu-card reveal">
                <div class="card-content">
                    <p class="card-title">Chicken Over Rice</p>
                    <p class="card-desc">New York style platter with Afghani rice, special chicken, and signature sauces.</p>
                    <div class="card-footer">
                        <p class="card-price">600 / 900 DA</p>
                    </div>
                </div>
            </div>
            <div class="menu-card reveal">
                <div class="card-content">
                    <p class="card-title">Nashville Chicken Burger</p>
                    <p class="card-desc">Breaded Nashville chicken, 2 slices of cheese, smoky sauce, coleslaw.</p>
                    <div class="card-footer">
                        <p class="card-price">700 DA</p>
                    </div>
                </div>
            </div>
        </div>"""
html = html.replace(old_highlights, new_highlights)

# Gallery replace
old_gallery = """            <h2>Instagram</h2>
            <p style="color: var(--light-gray); margin-top: 15px;">L’ambiance The Wall en images.</p>"""
new_gallery = """            <h2>Instagram</h2>
            <p style="color: var(--light-gray); margin-top: 15px;">Follow @thedonermansion for the latest updates.</p>"""
html = html.replace(old_gallery, new_gallery)

old_gallery_links = """        <div style="text-align: center; margin-top: 40px; display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <a href="https://www.facebook.com/thewallsnack/?ref=NONE_xav_ig_profile_page_web#" target="_blank" class="btn-outline">Voir Facebook</a>
            <a href="https://www.instagram.com/thewallsnack?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" target="_blank" class="btn-outline">Voir Instagram</a>
        </div>"""
new_gallery_links = """        <div style="text-align: center; margin-top: 40px; display: flex; gap: 16px; justify-content: center; flex-wrap: wrap;">
            <a href="https://www.instagram.com/thedonermansion" target="_blank" class="btn-outline">Rejoindre Instagram</a>
        </div>"""
html = html.replace(old_gallery_links, new_gallery_links)

# About Replace
old_about = """                <div class="section-header" style="text-align: left; margin-bottom: 30px;">
                    <h2 style="font-size: 3rem;">Notre histoire</h2>
                </div>
                <h3 style="color: var(--primary-orange); margin-bottom: 20px;">Gourmand, rapide, urbain</h3>
                <p>The Wall Snack & Resto propose une cuisine street-food généreuse avec des recettes modernes, des ingrédients soignés et un service rapide.</p>
                <p>Burgers, tacos, bowls, pizzas, grillades et accompagnements : tout est pensé pour une commande simple, claire et efficace.</p>
                <a href="#menu" class="btn-order">Découvrir le menu</a>"""
new_about = """                <div class="section-header" style="text-align: left; margin-bottom: 30px;">
                    <h2 style="font-size: 3rem;">Notre histoire</h2>
                </div>
                <h3 style="color: var(--primary-orange); margin-bottom: 20px;">The Burger Mansion Brand</h3>
                <p>The Döner Mansion is a modern fast-food concept created under the brand The Burger Mansion. We bring you bold flavors and satisfying portions inspired by international street-food.</p>
                <p>Enjoy our juicy burgers, Berlin-style döner wraps, rich New York platters, and crispy fried wings, prepared quickly for dine-in, takeaway or delivery. We are proud to serve customers globally with locations in Algeria and Sweden!</p>
                <a href="#menu" class="btn-order">Découvrir le menu</a>"""
html = html.replace(old_about, new_about)

# Location details
old_location = """            <div class="location-details">
                <h3 style="color: var(--primary-orange); margin-bottom: 20px;">The Wall Snack & Resto</h3>
                <p style="margin-bottom: 20px; color: var(--light-gray);">Retrouvez-nous à Dely Ibrahim, Alger. Service rapide et ambiance street-food.</p>
                <div style="margin-bottom: 15px;">
                    <p style="font-weight: bold; color: var(--white);">ADRESSE :</p>
                    <p style="color: var(--light-gray);">Dely Ibrahim, Alger</p>
                </div>
                <div style="margin-bottom: 30px;">
                    <p style="font-weight: bold; color: var(--white);">HORAIRES :</p>
                    <p style="color: var(--light-gray);">Tous les jours : 12h00 – 00h00</p>
                </div>
                <a href="https://maps.app.goo.gl/r6MNWi8BKuX97Pmg9" target="_blank" class="btn-order" style="display: inline-block; text-align: center;">Itinéraire</a>
            </div>"""
new_location = """            <div class="location-details">
                <h3 style="color: var(--primary-orange); margin-bottom: 20px;">The Döner Mansion</h3>
                <p style="margin-bottom: 20px; color: var(--light-gray);">Retrouvez-nous en Algérie et en Suède. Concept de street-food international.</p>
                <div style="margin-bottom: 15px;">
                    <p style="font-weight: bold; color: var(--white);">RÉSEAU INTERNATIONAL :</p>
                    <p style="color: var(--light-gray);">Algeria & Sweden</p>
                </div>
                <div style="margin-bottom: 30px;">
                    <p style="font-weight: bold; color: var(--white);">LIVRAISON :</p>
                    <p style="color: var(--light-gray);">Delivery service is available! Order food for delivery and receive your meals directly at home.</p>
                </div>
                <a href="https://maps.app.goo.gl/r6MNWi8BKuX97Pmg9" target="_blank" class="btn-order" style="display: inline-block; text-align: center;">Itinéraire (Algeria Location)</a>
            </div>"""
html = html.replace(old_location, new_location)

# Contact Replace
old_contact = """                <h3 style="color: var(--primary-orange); margin-bottom: 20px;">Nous contacter</h3>
                <p style="color: var(--light-gray); margin-bottom: 30px;">Commandes rapides par téléphone ou WhatsApp. Réponse directe via Facebook et Instagram.</p>
                
                <div style="margin-bottom: 20px;">
                    <p style="font-weight: bold; color: var(--white);">TÉLÉPHONE :</p>
                    <a href="tel:0555219684" style="color: var(--primary-orange); font-size: 1.2rem; text-decoration: none;">0555 21 96 84</a>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <p style="font-weight: bold; color: var(--white);">RÉSEAUX :</p>
                    <div class="social-links" style="margin-top: 10px;">
                        <a href="https://www.facebook.com/thewallsnack/?ref=NONE_xav_ig_profile_page_web#" target="_blank" style="color: var(--white); font-size: 1.5rem; margin-right: 20px;"><i class="fab fa-facebook"></i></a>
                        <a href="https://www.instagram.com/thewallsnack?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" target="_blank" style="color: var(--white); font-size: 1.5rem; margin-right: 20px;"><i class="fab fa-instagram"></i></a>
                        <a href="https://wa.me/213555219684" target="_blank" style="color: var(--white); font-size: 1.5rem;"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
                <div style="margin-bottom: 20px;">
                    <p style="font-weight: bold; color: var(--white);">ADRESSE :</p>
                    <p style="color: var(--light-gray);">Dely Ibrahim, Alger</p>
                </div>"""
new_contact = """                <h3 style="color: var(--primary-orange); margin-bottom: 20px;">Nous contacter</h3>
                <p style="color: var(--light-gray); margin-bottom: 30px;">Call us to place an order for takeaway or home delivery. Follow us on Instagram for updates!</p>
                
                <div style="margin-bottom: 20px;">
                    <p style="font-weight: bold; color: var(--white);">TÉLÉPHONE (Order & Info) :</p>
                    <a href="tel:0796663395" style="color: var(--primary-orange); font-size: 1.2rem; text-decoration: none;">07 96 66 33 95</a>
                </div>
                
                <div style="margin-bottom: 20px;">
                    <p style="font-weight: bold; color: var(--white);">RÉSEAUX :</p>
                    <div class="social-links" style="margin-top: 10px;">
                        <a href="https://www.instagram.com/thedonermansion" target="_blank" style="color: var(--white); font-size: 1.5rem; margin-right: 20px;"><i class="fab fa-instagram"></i></a>
                        <a href="https://wa.me/213796663395" target="_blank" style="color: var(--white); font-size: 1.5rem;"><i class="fab fa-whatsapp"></i></a>
                    </div>
                </div>
                <div style="margin-bottom: 20px;">
                    <p style="font-weight: bold; color: var(--white);">LOCATIONS :</p>
                    <p style="color: var(--light-gray);">Algeria & Sweden</p>
                </div>"""
html = html.replace(old_contact, new_contact)

old_sidebar_contact = """        <div style="display: grid; gap: 12px;">
            <a href="tel:0555219684" class="btn-order" style="width: 100%; text-align: center; display: block;">Commander par téléphone</a>
            <a href="https://wa.me/213555219684" target="_blank" class="btn-outline" style="width: 100%; text-align: center; display: block;">Commander sur WhatsApp</a>
        </div>"""
new_sidebar_contact = """        <div style="display: grid; gap: 12px;">
            <a href="tel:0796663395" class="btn-order" style="width: 100%; text-align: center; display: block;">Commander par téléphone</a>
            <a href="https://wa.me/213796663395" target="_blank" class="btn-outline" style="width: 100%; text-align: center; display: block;">Commander sur WhatsApp</a>
        </div>"""
html = html.replace(old_sidebar_contact, new_sidebar_contact)

old_footer_logo = """                <img src="images/logo.jpg" alt="The Döner Mansion Logo" style="height: 70px; margin-bottom: 20px;">
                <p style="color: var(--gray-text);">The Wall Snack & Resto : street-food moderne, rapide et généreuse.</p>"""
new_footer_logo = """                <img src="images/logo.jpg" alt="The Döner Mansion Logo" style="height: 70px; margin-bottom: 20px;">
                <p style="color: var(--gray-text);">The Döner Mansion : Berlin-style Döner, juicy burgers, and New York street food platters. Delivered fast.</p>"""
html = html.replace(old_footer_logo, new_footer_logo)

old_footer_social = """            <div>
                <h4 style="color: var(--white); font-family: 'Oswald'; text-transform: uppercase; margin-bottom: 20px;">Réseaux</h4>
                <p style="color: var(--light-gray); margin-bottom: 20px;">Suivez nos actus et promos.</p>
                <div class="social-links">
                    <a href="https://www.facebook.com/thewallsnack/?ref=NONE_xav_ig_profile_page_web#" target="_blank" style="color: var(--white); font-size: 1.2rem; margin-right: 15px;"><i class="fab fa-facebook"></i> The Wall Snack</a>
                    <a href="https://www.instagram.com/thewallsnack?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==" target="_blank" style="color: var(--white); font-size: 1.2rem; margin-right: 15px;"><i class="fab fa-instagram"></i> @thewallsnack</a>
                </div>
            </div>
        </div>
        <div style="text-align: center; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.05); color: var(--gray-text); font-size: 0.8rem;">
            &copy; 2026 The Wall Snack & Resto. Tous droits réservés.
        </div>"""
new_footer_social = """            <div>
                <h4 style="color: var(--white); font-family: 'Oswald'; text-transform: uppercase; margin-bottom: 20px;">Réseaux</h4>
                <p style="color: var(--light-gray); margin-bottom: 20px;">Follow @thedonermansion.</p>
                <div class="social-links">
                    <a href="https://www.instagram.com/thedonermansion" target="_blank" style="color: var(--white); font-size: 1.2rem; margin-right: 15px;"><i class="fab fa-instagram"></i> @thedonermansion</a>
                </div>
            </div>
        </div>
        <div style="text-align: center; padding-top: 30px; border-top: 1px solid rgba(255,255,255,0.05); color: var(--gray-text); font-size: 0.8rem;">
            &copy; 2026 The Döner Mansion. Tous droits réservés.
        </div>"""
html = html.replace(old_footer_social, new_footer_social)

# Menu replace regex
new_menu_js = """    const menuData = [
        {
            category: "doner",
            title: "DÖNER",
            note: "Berlin style street food",
            items: [
                { id: "doner-classic", name: "Döner Classic", price: 800, description: "180g döner, sautéed and seasoned vegetables (Berlin style), lettuce, tomato, onion, cucumber, mozzarella with herbs, herb sauce, and cocktail sauce." },
                { id: "doner-spicy", name: "Döner Spicy & Strong", price: 800, description: "180g döner, sautéed and seasoned vegetables (Berlin style), lettuce, onion, marinated chili, red cabbage, mozzarella with herbs, herb sauce, cocktail sauce, and spicy sauce." },
                { id: "durum-wrap", name: "Durum Wrap", price: 800, description: "Durum bread, 180g döner, sautéed and seasoned vegetables (Berlin style), lettuce, tomato, onion, cucumber, mozzarella with herbs, herb sauce, and cocktail sauce." }
            ]
        },
        {
            category: "assiettes",
            title: "ASSIETTES (Platters)",
            note: "New York Street Food Style",
            items: [
                { id: "chicken-over-rice", name: "Chicken Over Rice (NEW YORK)", price: 900, description: "Afghani rice, special chicken, herb sauce, spicy sauce, lettuce, tomato, onion, cucumber, and chickpeas. (600/900 DA)" },
                { id: "fried-chicken-over-rice", name: "Fried Chicken Over Rice", price: 900, description: "Afghani rice, Nashville chicken, herb sauce, spicy sauce, sautéed vegetables, and marinated chili. (600/900 DA)" }
            ]
        },
        {
            category: "burger",
            title: "BURGER",
            items: [
                { id: "mansion-classic", name: "The Mansion Classic", price: 700, description: "180g smash beef, 4 slices of cheese, classic sauce, lettuce, tomato, onion, ketchup, and artisanal pickles. (500/700 DA)" },
                { id: "spicy-one", name: "The Spicy One", price: 750, description: "180g smash beef, 4 slices of cheese, spicy sauce, lettuce, onion & caramelized onion, and artisanal marinated chili. (550/750 DA)" },
                { id: "smokey-bbq", name: "The Smokey Barbecue", price: 800, description: "180g smash beef, 4 slices of cheese, smoky sauce, caramelized onion, and breaded mozzarella. (600/800 DA)" },
                { id: "nashville-chicken", name: "Nashville Chicken Burger", price: 700, description: "Breaded chicken, 2 slices of cheese, smoky sauce, coleslaw, and artisanal pickles." },
                { id: "the-egg", name: "The Egg", price: 800, description: "180g beef, cheddar, lettuce, grilled tomatoes, egg, and classic sauce. (600/800 DA)" },
                { id: "royal-cheese", name: "The Royal Cheese", price: 950, description: "180g beef, gruyère, camembert, caramelized onions, ketchup, and smoky sauce. (700/950 DA)" },
                { id: "menu-kids", name: "Menu Kids", price: 750, description: "Cheeseburger, small fries, and a drink." }
            ]
        },
        {
            category: "hot-wings",
            title: "HOT WINGS",
            note: "All orders include 5 pieces and ranch sauce.",
            items: [
                { id: "wings-nashville", name: "Nashville Spicy", price: 500, description: "5 pieces + ranch sauce" },
                { id: "wings-lemon", name: "Lemon Garlic", price: 500, description: "5 pieces + ranch sauce" },
                { id: "wings-buffalo", name: "Classic Buffalo", price: 500, description: "5 pieces + ranch sauce" },
                { id: "wings-smokey", name: "Smokey BBQ", price: 500, description: "5 pieces + ranch sauce" }
            ]
        },
        {
            category: "frites-special",
            title: "FRITES SPÉCIAL (Loaded Fries)",
            items: [
                { id: "frites-poulet", name: "Frites Poulet", price: 450, description: "Fries, crispy chicken, marinated chili, onion, cheese sauce, and classic sauce." },
                { id: "frites-cheese-doner", name: "Frites Cheese Döner", price: 450, description: "Fries, döner meat, caramelized onion, cheese sauce, and smoky sauce." },
                { id: "frites-viande", name: "Frites Viande", price: 500, description: "Fries, 90g beef, caramelized onion, cheese sauce, and smoky sauce." },
                { id: "frites-epicee", name: "Frites Épicée (Spicy Fries)", price: 200, description: "Spicy seasoned fries." },
                { id: "frites-cheese", name: "Frites + Sauce Cheese", price: 250, description: "Fries with cheese sauce." }
            ]
        },
        {
            category: "sauces",
            title: "NOS SAUCES",
            items: [
                { id: "sauce-herbe", name: "Sauce Herbe", price: 50, description: "" },
                { id: "sauce-cocktail", name: "Sauce Cocktail", price: 50, description: "" },
                { id: "sauce-spicy", name: "Sauce Spicy", price: 50, description: "" },
                { id: "sauce-cheese", name: "Sauce Cheese", price: 50, description: "" }
            ]
        },
        {
            category: "boisson",
            title: "BOISSON (Drinks)",
            items: [
                { id: "canette", name: "Canette (Soda Can)", price: 100, description: "" },
                { id: "jus", name: "Jus (Juice)", price: 100, description: "" },
                { id: "eau-minerale", name: "Eau Minérale (Mineral Water)", price: 50, description: "" }
            ]
        }
    ];"""

pattern = re.compile(r"    const menuData = \[\s*\{.*?\}\s*\];", re.DOTALL)
html = pattern.sub(new_menu_js, html)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(html)

print("HTML content updated successfully.")
