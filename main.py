import flet as ft
import math


def main(page: ft.Page):
    page.title = "Daniel Mathew | Portfolio"
    page.bgcolor = "#08090C"
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.fonts = {
        "Playfair": "https://fonts.gstatic.com/s/playfairdisplay/v37/nuFiD-vYSZviVYUb_rj3ij__anPXDTzYgEM86xRbPQ.woff2",
        "DM Sans": "https://fonts.gstatic.com/s/dmsans/v15/rP2Hp2ywxg089UriCZa4ET-DNl0.woff2",
    }
    page.theme = ft.Theme(font_family="DM Sans")

    # ── COLOURS ──────────────────────────────────────────────────────────────
    BG       = "#08090C"
    SURFACE  = "#0F1117"
    SURF2    = "#161B25"
    GOLD     = "#C8A96E"
    GOLD_DIM = "#C8A96E22"
    MUTED    = "#7A8494"
    TEXT     = "#E8EDF5"
    GREEN    = "#3FB950"

    # ── HELPERS ──────────────────────────────────────────────────────────────
    def gold_line():
        return ft.Container(width=44, height=2, bgcolor=GOLD, border_radius=2, margin=ft.margin.only(bottom=20))

    def section_label(text):
        return ft.Text(text.upper(), size=11, color=GOLD, weight=ft.FontWeight.W_500,
                       letter_spacing=3, font_family="DM Sans")

    def section_title(text):
        return ft.Text(text, size=32, color=TEXT, weight=ft.FontWeight.BOLD,
                       font_family="Playfair", selectable=True)

    def chip(label, color=GOLD):
        return ft.Container(
            content=ft.Text(label, size=11, color=color),
            padding=ft.padding.symmetric(horizontal=10, vertical=4),
            border=ft.border.all(0.5, f"{color}44"),
            border_radius=6,
            bgcolor=f"{color}15",
        )

    def divider():
        return ft.Divider(height=1, color="#FFFFFF0F")

    def nav_item(label, section_id):
        def go(_):
            page.scroll_to(key=section_id, duration=600)
        return ft.TextButton(
            label,
            style=ft.ButtonStyle(color={ft.ControlState.DEFAULT: MUTED, ft.ControlState.HOVERED: GOLD}),
            on_click=go,
        )

    # ── NAV ──────────────────────────────────────────────────────────────────
    nav = ft.Container(
        content=ft.Row(
            [
                ft.Text("D. Mathew", size=16, color=GOLD, font_family="Playfair", weight=ft.FontWeight.BOLD),
                ft.Row([
                    nav_item("About", "about"),
                    nav_item("Timeline", "timeline"),
                    nav_item("MATLAB Hub", "matlab"),
                    nav_item("Blog", "blog"),
                    nav_item("GitHub", "github"),
                    nav_item("Contact", "contact"),
                ], spacing=4),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        padding=ft.padding.symmetric(horizontal=60, vertical=16),
        bgcolor="#08090CEE",
        border=ft.border.only(bottom=ft.BorderSide(0.5, "#C8A96E44")),
    )

    # ── HERO ─────────────────────────────────────────────────────────────────
    hero = ft.Container(
        key="home",
        content=ft.Column([
            ft.Container(
                content=ft.Text("✦  Mining Engineer · Developer · Namibia", size=12, color=GOLD, letter_spacing=2),
                padding=ft.padding.symmetric(horizontal=16, vertical=6),
                border=ft.border.all(0.5, "#C8A96E44"),
                border_radius=50,
                bgcolor=GOLD_DIM,
            ),
            ft.Container(height=20),
            ft.Text("DANIEL", size=64, color=TEXT, font_family="Playfair", weight=ft.FontWeight.BOLD, height=1.05),
            ft.Text("MATHEW", size=64, color=GOLD, font_family="Playfair", italic=True, height=1.05),
            ft.Container(height=10),
            ft.Container(
                content=ft.Text("Mining Engineering · MATLAB Developer · App Creator",
                                size=13, color=MUTED, letter_spacing=1.5),
                border=ft.border.only(left=ft.BorderSide(2, GOLD)),
                padding=ft.padding.only(left=12),
            ),
            ft.Container(height=16),
            ft.Text(
                "A driven engineering student from Ongwediva, Namibia, combining the rigour of Mining Engineering "
                "with modern computational skills and building tools that solve real problems.",
                size=15, color=MUTED, width=520,
            ),
            ft.Container(height=20),
            ft.Container(
                content=ft.Column([
                    ft.Row([ft.Text("📧", size=14), ft.Text("danieldanielm09@gmail.com", size=13, color=TEXT)], spacing=8),
                    ft.Row([ft.Text("📱", size=14), ft.Text("+264 81 716 0236", size=13, color=TEXT)], spacing=8),
                    ft.Row([ft.Text("📍", size=14), ft.Text("Ongwediva, Namibia", size=13, color=TEXT)], spacing=8),
                    ft.Row([ft.Text("🎓", size=14), ft.Text("University of Namibia — Mining Engineering, Year 2", size=13, color=TEXT)], spacing=8),
                ], spacing=8),
                padding=ft.padding.all(16),
                bgcolor="#FFFFFF08",
                border=ft.border.all(0.5, "#FFFFFF14"),
                border_radius=12,
            ),
            ft.Container(height=24),
            ft.Row([
                ft.ElevatedButton(
                    "My Certificates",
                    bgcolor=GOLD, color=BG,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    on_click=lambda _: page.scroll_to(key="matlab", duration=600),
                ),
                ft.OutlinedButton(
                    "Get in Touch",
                    style=ft.ButtonStyle(
                        color={ft.ControlState.DEFAULT: TEXT, ft.ControlState.HOVERED: GOLD},
                        side={ft.ControlState.DEFAULT: ft.BorderSide(0.5, "#FFFFFF33"),
                              ft.ControlState.HOVERED: ft.BorderSide(0.5, GOLD)},
                        shape=ft.RoundedRectangleBorder(radius=8),
                    ),
                    on_click=lambda _: page.scroll_to(key="contact", duration=600),
                ),
            ], spacing=12),
        ], spacing=0),
        padding=ft.padding.only(left=80, right=80, top=120, bottom=80),
        bgcolor=BG,
    )

    # ── ABOUT ────────────────────────────────────────────────────────────────
    def info_card(label, value):
        return ft.Container(
            content=ft.Column([
                ft.Text(label.upper(), size=10, color=MUTED, letter_spacing=2),
                ft.Text(value, size=13, color=TEXT, weight=ft.FontWeight.W_500),
            ], spacing=3),
            padding=ft.padding.all(14),
            bgcolor=SURF2,
            border=ft.border.all(0.5, "#FFFFFF10"),
            border_radius=10,
            expand=True,
        )

    about = ft.Container(
        key="about",
        content=ft.Column([
            section_label("Who I Am"),
            ft.Container(height=6),
            section_title("About Me"),
            gold_line(),
            ft.Row([
                ft.Column([
                    ft.Text(
                        "I am Daniel Mathew, a second year Mining Engineering student at the University of Namibia. "
                        "Growing up in Ongwediva, I have always been fascinated by the ground beneath our feet and "
                        "the engineering that makes it possible to extract value from it responsibly.",
                        size=14, color=MUTED, width=480,
                    ),
                    ft.Container(height=12),
                    ft.Text(
                        "What sets me apart is that I refuse to stay within the traditional boundaries of my degree. "
                        "I taught myself MATLAB App Designer, built a working Android application, and am now learning "
                        "Python through Flet to create web applications. Engineering is not just what I study — it is "
                        "how I think.",
                        size=14, color=MUTED, width=480,
                    ),
                    ft.Container(height=20),
                    ft.Row([
                        info_card("Program", "Mining Engineering"),
                        info_card("Year", "2nd Year"),
                    ], spacing=10),
                    ft.Container(height=10),
                    ft.Row([
                        info_card("Institution", "UNAM"),
                        info_card("Location", "Ongwediva, Namibia"),
                    ], spacing=10),
                ], expand=True),
                ft.Column([
                    ft.Text("SKILLS", size=11, color=GOLD, letter_spacing=2, weight=ft.FontWeight.W_500),
                    ft.Container(height=10),
                    ft.Wrap([
                        chip("Python"), chip("Flet"), chip("MATLAB"),
                        chip("App Designer"), chip("Android Dev"), chip("Blast Design"),
                        chip("Firebase"), chip("HTML/CSS"), chip("Git / GitHub"),
                    ], spacing=6, run_spacing=6),
                    ft.Container(height=24),
                    ft.Container(
                        content=ft.Row([
                            ft.Column([
                                ft.Text("8", size=32, color=GOLD, font_family="Playfair", weight=ft.FontWeight.BOLD),
                                ft.Text("MATLAB Courses", size=11, color=MUTED),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
                            ft.VerticalDivider(color="#C8A96E44"),
                            ft.Column([
                                ft.Text("5", size=32, color=GOLD, font_family="Playfair", weight=ft.FontWeight.BOLD),
                                ft.Text("Projects Built", size=11, color=MUTED),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
                            ft.VerticalDivider(color="#C8A96E44"),
                            ft.Column([
                                ft.Text("2", size=32, color=GOLD, font_family="Playfair", weight=ft.FontWeight.BOLD),
                                ft.Text("Apps Deployed", size=11, color=MUTED),
                            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True),
                        ], spacing=0),
                        border=ft.border.all(0.5, "#C8A96E44"),
                        border_radius=12,
                        bgcolor=SURF2,
                        padding=ft.padding.symmetric(vertical=20),
                    ),
                ], expand=True),
            ], spacing=60, vertical_alignment=ft.CrossAxisAlignment.START),
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=80, vertical=80),
        bgcolor=SURFACE,
    )

    # ── PROJECT TIMELINE ─────────────────────────────────────────────────────
    timeline_entries = [
        ("Week 1", "Project Kickoff and Planning",
         "The team of 20 students was introduced to MechTek, our group engineering application. "
         "I volunteered to work on the Mining module, specifically the blast design calculator. "
         "We set up the shared GitHub repository and agreed on branching conventions."),
        ("Week 2", "Repository Setup and Firebase Integration",
         "I configured the Firebase Realtime Database connection for our module, wrote the initial "
         "firebase.js configuration file, and pushed the first verified commit. I also updated "
         ".gitignore to keep credentials out of version control."),
        ("Week 3", "Core Mining Calculator Logic",
         "I built the main calculation engine for the blast design section — covering ore tonnage, "
         "powder factor, charge per hole, and radius from hole diameter. Every formula was verified "
         "against real mining engineering references before being committed."),
        ("Week 4", "UI Components and Input Validation",
         "I designed the user interface for the Mining module input screens, added real-time input "
         "validation, and connected the calculation engine to the display layer. I raised a pull "
         "request and it was merged after a peer code review."),
        ("Week 5", "Blog Videos and Technical Documentation",
         "I recorded two walkthrough videos for the Technical Blog section demonstrating the "
         "application in use. I also wrote the technical explanation posts that accompany the videos, "
         "making sure the concepts were explained in plain language alongside proper notation."),
        ("Week 6", "Final Testing and Portfolio Completion",
         "I ran end-to-end testing on my module, fixed two edge-case bugs found during peer review, "
         "and finalised this portfolio. The app was deployed as a live Flet web application and the "
         "GitHub evidence was compiled and documented."),
    ]

    def timeline_card(week, title, desc):
        return ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Container(
                        content=ft.Text(week, size=10, color=GOLD, letter_spacing=2, weight=ft.FontWeight.W_600),
                        padding=ft.padding.symmetric(horizontal=12, vertical=6),
                        border=ft.border.all(0.5, "#C8A96E44"),
                        border_radius=20,
                        bgcolor=GOLD_DIM,
                    ),
                ], width=90),
                ft.Container(width=24),
                ft.Column([
                    ft.Text(title, size=15, color=TEXT, weight=ft.FontWeight.W_600),
                    ft.Container(height=6),
                    ft.Text(desc, size=13, color=MUTED, width=600),
                ], expand=True),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            padding=ft.padding.all(20),
            bgcolor=SURF2,
            border=ft.border.all(0.5, "#FFFFFF0A"),
            border_radius=12,
            margin=ft.margin.only(bottom=12),
        )

    timeline_section = ft.Container(
        key="timeline",
        content=ft.Column([
            section_label("Weekly Log"),
            ft.Container(height=6),
            section_title("Project Timeline"),
            gold_line(),
            ft.Text(
                "Below is a week by week log of my specific contributions to the MechTek group application. "
                "Each entry reflects what I personally worked on, committed, and delivered.",
                size=14, color=MUTED, width=640,
            ),
            ft.Container(height=28),
            ft.Column([timeline_card(w, t, d) for w, t, d in timeline_entries], spacing=0),
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=80, vertical=80),
        bgcolor=BG,
    )

    # ── MATLAB ACHIEVEMENT HUB ───────────────────────────────────────────────
    courses = [
        ("MATLAB Onramp", "MathWorks · 2 hrs", "100%"),
        ("MATLAB Fundamentals", "MathWorks · 6 hrs", "100%"),
        ("MATLAB Programming Techniques", "MathWorks · 8 hrs", "94%"),
        ("Data Processing and Visualization", "MathWorks · 5 hrs", "100%"),
        ("App Building with MATLAB", "MathWorks · 4 hrs", "100%"),
        ("Signal Processing Onramp", "MathWorks · 2 hrs", "100%"),
        ("Image Processing with MATLAB", "MathWorks · 4 hrs", "94%"),
        ("Machine Learning Onramp", "MathWorks · 2 hrs", "100%"),
    ]

    def cert_card(name, meta, score):
        color = GREEN if score == "100%" else GOLD
        return ft.Container(
            content=ft.Row([
                ft.Container(
                    content=ft.Text("🎓", size=18),
                    width=44, height=44,
                    bgcolor=GOLD_DIM,
                    border=ft.border.all(0.5, "#C8A96E44"),
                    border_radius=8,
                    alignment=ft.alignment.center,
                ),
                ft.Container(width=12),
                ft.Column([
                    ft.Text(name, size=13, color=TEXT, weight=ft.FontWeight.W_500),
                    ft.Text(meta, size=11, color=MUTED),
                    ft.Container(
                        content=ft.Text(score, size=11, color=color, weight=ft.FontWeight.W_600),
                        margin=ft.margin.only(top=4),
                        padding=ft.padding.symmetric(horizontal=8, vertical=2),
                        bgcolor=f"{color}20",
                        border=ft.border.all(0.5, f"{color}40"),
                        border_radius=4,
                    ),
                ], spacing=2, expand=True),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
            padding=ft.padding.all(16),
            bgcolor=SURFACE,
            border=ft.border.all(0.5, "#FFFFFF0A"),
            border_radius=12,
            expand=True,
        )

    matlab_section = ft.Container(
        key="matlab",
        content=ft.Column([
            section_label("Achievement Hub"),
            ft.Container(height=6),
            section_title("MATLAB Courses"),
            gold_line(),
            ft.Text(
                "I completed all 8 self-paced courses on the MathWorks Learning Center as part of this semester's "
                "requirements. Each course built on the last, taking me from the basics of scripting all the way "
                "through to image processing and machine learning foundations.",
                size=14, color=MUTED, width=640,
            ),
            ft.Container(height=28),
            ft.Column([
                ft.Row([cert_card(*courses[i]), ft.Container(width=12), cert_card(*courses[i+1])], spacing=0)
                for i in range(0, len(courses), 2)
            ], spacing=12),
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=80, vertical=80),
        bgcolor=SURFACE,
    )

    # ── TECHNICAL BLOG ───────────────────────────────────────────────────────
    def blog_post(emoji, title, body_paragraphs, video_path=None, tags=None):
        video_widget = []
        if video_path:
            video_widget = [
                ft.Container(height=16),
                ft.Container(
                    content=ft.Column([
                        ft.Text("▶  Demo Video", size=11, color=GOLD, letter_spacing=1.5),
                        ft.Container(height=8),
                        ft.Video(
                            playlist=[ft.VideoMedia(video_path)],
                            width=680,
                            height=360,
                            fit=ft.ImageFit.CONTAIN,
                            autoplay=False,
                            show_controls=True,
                        ),
                    ]),
                    bgcolor=SURF2,
                    border=ft.border.all(0.5, "#C8A96E44"),
                    border_radius=12,
                    padding=ft.padding.all(16),
                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                ),
            ]

        tag_row = []
        if tags:
            tag_row = [ft.Container(height=16), ft.Row([chip(t) for t in tags], wrap=True, spacing=6)]

        paragraphs = [ft.Text(p, size=14, color=MUTED, width=680) for p in body_paragraphs]
        spaced_paragraphs = []
        for i, p in enumerate(paragraphs):
            spaced_paragraphs.append(p)
            if i < len(paragraphs) - 1:
                spaced_paragraphs.append(ft.Container(height=12))

        return ft.Container(
            content=ft.Column([
                ft.Row([
                    ft.Text(emoji, size=28),
                    ft.Container(width=12),
                    ft.Column([
                        ft.Text(title, size=18, color=TEXT, weight=ft.FontWeight.BOLD, font_family="Playfair"),
                    ]),
                ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
                ft.Container(height=16),
                *spaced_paragraphs,
                *video_widget,
                *tag_row,
            ], spacing=0),
            padding=ft.padding.all(28),
            bgcolor=SURF2,
            border=ft.border.all(0.5, "#FFFFFF0A"),
            border_radius=16,
            margin=ft.margin.only(bottom=20),
        )

    blog_section = ft.Container(
        key="blog",
        content=ft.Column([
            section_label("Confidence in Concepts"),
            ft.Container(height=6),
            section_title("Technical Blog"),
            gold_line(),
            ft.Text(
                "This section is where I explain the programming concepts that shaped how I think as an engineer. "
                "Each post is honest about what I found difficult and what made things click.",
                size=14, color=MUTED, width=640,
            ),
            ft.Container(height=28),

            blog_post(
                "⚙️",
                "How the MechTek App Actually Works",
                [
                    "When I first joined the MechTek project I assumed I would be writing a few functions and "
                    "calling it a day. What I quickly discovered is that building a real application used by 20 "
                    "people simultaneously requires thinking about structure before you write a single line of code.",

                    "The app is built around a Firebase Realtime Database at its core. Every module, whether it "
                    "handles mining calculations, civil engineering tools, or metallurgical lookups, connects to "
                    "the same backend. My job was to make sure the Mining module spoke to that backend correctly "
                    "without breaking anything else.",

                    "The most valuable lesson from this project was learning to read other people's code before "
                    "writing your own. I spent the first two days just understanding how the existing modules "
                    "were structured. That investment paid off because my integration was clean on the first "
                    "pull request without requiring rewrites.",
                ],
                video_path="/mnt/user-data/uploads/project_2__1_.mp4",
                tags=["Firebase", "Python", "Flet", "Architecture", "MechTek"],
            ),

            blog_post(
                "💥",
                "Blast Design Maths — From Formula to Code",
                [
                    "One of the most satisfying moments in this semester was writing a calculation in MATLAB that "
                    "I had only ever seen in a textbook before. The blast design calculator required me to turn "
                    "real mining engineering formulas into working code.",

                    "The powder factor, which tells a blast crew how much explosive to use per tonne of rock, "
                    "sounds straightforward until you realise every variable feeds into every other. Hole "
                    "diameter determines the charge radius which determines the charge mass which feeds into "
                    "the total explosive weight which then divides against the ore tonnage.",

                    "Writing this in code forced me to understand the formula more deeply than I ever did "
                    "reading it on a page. When the numbers matched the textbook example I had chosen as a "
                    "test case, that was a genuinely exciting moment. The video below walks through the "
                    "application in action.",
                ],
                video_path="/mnt/user-data/uploads/project_3.mp4",
                tags=["MATLAB", "Blast Design", "Mining Engineering", "App Designer"],
            ),

            blog_post(
                "🔥",
                "What Firebase Taught Me About Real Applications",
                [
                    "Before this project, I thought databases were something advanced developers used in big "
                    "companies. Firebase showed me that connecting an app to a live database is actually "
                    "very approachable once you understand the authentication flow.",

                    "The key insight is that Firebase does not care what your app looks like. It just stores "
                    "and retrieves JSON. That simplicity is powerful because it means you can focus on what "
                    "your app needs to do rather than spending weeks on database administration.",

                    "The moment I saw a value I had entered on one device appear on another device in real "
                    "time, without refreshing, is the moment I understood why real-time databases matter. "
                    "That experience changed how I think about software and data.",
                ],
                tags=["Firebase", "Real-time DB", "JSON", "Authentication"],
            ),
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=80, vertical=80),
        bgcolor=BG,
    )

    # ── GITHUB EVIDENCE ──────────────────────────────────────────────────────
    commits = [
        ("b631dcb", "Update package.json", "Jun 9, 2026", "Verified"),
        ("4210166", "Update README.md", "Jun 8, 2026", "Verified"),
        ("d9bf963", "Update .gitignore", "Jun 8, 2026", "Verified"),
        ("7e6fa16", "Update index.js", "Jun 8, 2026", "Verified"),
        ("00fa891", "Update firebase.js", "Jun 8, 2026", "Verified"),
    ]

    def commit_row(sha, message, date, status):
        return ft.Container(
            content=ft.Row([
                ft.Column([
                    ft.Text(message, size=13, color=TEXT, weight=ft.FontWeight.W_500),
                    ft.Text(f"danieldanielm09-max · {date}", size=11, color=MUTED),
                ], expand=True),
                ft.Container(
                    content=ft.Text(status, size=10, color=GREEN),
                    padding=ft.padding.symmetric(horizontal=10, vertical=4),
                    border=ft.border.all(0.5, f"{GREEN}55"),
                    border_radius=20,
                    bgcolor=f"{GREEN}15",
                ),
                ft.Container(width=12),
                ft.Container(
                    content=ft.Text(sha, size=11, color=MUTED, font_family="monospace"),
                    padding=ft.padding.symmetric(horizontal=10, vertical=4),
                    bgcolor=SURF2,
                    border_radius=6,
                ),
            ], vertical_alignment=ft.CrossAxisAlignment.CENTER),
            padding=ft.padding.symmetric(horizontal=20, vertical=16),
            bgcolor=SURFACE,
            border=ft.border.all(0.5, "#FFFFFF0A"),
            border_radius=10,
            margin=ft.margin.only(bottom=8),
        )

    github_section = ft.Container(
        key="github",
        content=ft.Column([
            section_label("GitHub Evidence"),
            ft.Container(height=6),
            section_title("My Contributions"),
            gold_line(),
            ft.Text(
                "The MechTek repository is a 20-person shared codebase. Here is verifiable evidence of my "
                "individual commits to the main branch, all of which are signed and verified.",
                size=14, color=MUTED, width=640,
            ),
            ft.Container(height=12),
            ft.Container(
                content=ft.Row([
                    ft.Text("📁", size=14),
                    ft.Text("224032909/MechTek", size=13, color=GOLD, weight=ft.FontWeight.W_500),
                    ft.Text("· main branch", size=12, color=MUTED),
                ], spacing=8),
                padding=ft.padding.symmetric(horizontal=16, vertical=10),
                bgcolor=SURF2,
                border=ft.border.all(0.5, "#C8A96E33"),
                border_radius=8,
            ),
            ft.Container(height=20),

            ft.Text("COMMIT HISTORY", size=11, color=GOLD, letter_spacing=2),
            ft.Container(height=10),
            ft.Column([commit_row(*c) for c in commits], spacing=0),

            ft.Container(height=32),
            ft.Text("PULL REQUESTS & REVIEWS", size=11, color=GOLD, letter_spacing=2),
            ft.Container(height=10),
            ft.Container(
                content=ft.Column([
                    ft.Row([
                        ft.Text("🟢", size=14),
                        ft.Column([
                            ft.Text("feat: Mining module blast design calculator", size=13, color=TEXT, weight=ft.FontWeight.W_500),
                            ft.Text("Opened and merged by danieldanielm09-max · Jun 8, 2026", size=11, color=MUTED),
                        ], expand=True),
                        ft.Container(
                            content=ft.Text("Merged", size=10, color="#A371F7"),
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            border=ft.border.all(0.5, "#A371F755"),
                            border_radius=20,
                            bgcolor="#A371F715",
                        ),
                    ], vertical_alignment=ft.CrossAxisAlignment.START),
                    ft.Divider(height=1, color="#FFFFFF0A"),
                    ft.Row([
                        ft.Text("💬", size=14),
                        ft.Column([
                            ft.Text("Code review on Civil module: input sanitization fix", size=13, color=TEXT, weight=ft.FontWeight.W_500),
                            ft.Text("Review submitted by danieldanielm09-max · Jun 7, 2026", size=11, color=MUTED),
                        ], expand=True),
                        ft.Container(
                            content=ft.Text("Reviewed", size=10, color=GOLD),
                            padding=ft.padding.symmetric(horizontal=10, vertical=4),
                            border=ft.border.all(0.5, "#C8A96E55"),
                            border_radius=20,
                            bgcolor=GOLD_DIM,
                        ),
                    ], vertical_alignment=ft.CrossAxisAlignment.START),
                ], spacing=16),
                padding=ft.padding.all(20),
                bgcolor=SURFACE,
                border=ft.border.all(0.5, "#FFFFFF0A"),
                border_radius=12,
            ),

            ft.Container(height=32),
            ft.Text("IMPACT SUMMARY", size=11, color=GOLD, letter_spacing=2),
            ft.Container(height=10),
            ft.Container(
                content=ft.Column([
                    ft.Text(
                        "My primary contribution to MechTek was designing and implementing the Mining Engineering module. "
                        "This module allows users to input blast design parameters and instantly receive calculated outputs "
                        "including powder factor, ore tonnage, and explosive charge per hole.",
                        size=14, color=MUTED,
                    ),
                    ft.Container(height=12),
                    ft.Text(
                        "Before my module was added, the app had no functionality for mining operations. My code filled "
                        "that gap and gave the Mining Engineering students in our group a working tool they could relate "
                        "to their actual coursework. I also contributed to the project's documentation by updating "
                        "README.md with setup instructions and by configuring the Firebase connection that other "
                        "modules depended on.",
                        size=14, color=MUTED,
                    ),
                ]),
                padding=ft.padding.all(20),
                bgcolor=SURF2,
                border=ft.border.all(0.5, "#C8A96E22"),
                border_radius=12,
                border=ft.border.only(left=ft.BorderSide(3, GOLD)),
            ),
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=80, vertical=80),
        bgcolor=SURFACE,
    )

    # ── CONTACT ──────────────────────────────────────────────────────────────
    contact_section = ft.Container(
        key="contact",
        content=ft.Column([
            section_label("Let's Connect"),
            ft.Container(height=6),
            section_title("Get in Touch"),
            gold_line(),
            ft.Row([
                ft.Column([
                    ft.Text("Open to opportunities", size=18, color=TEXT, font_family="Playfair"),
                    ft.Container(height=12),
                    ft.Text(
                        "Whether you are a lecturer, industry professional, potential collaborator, or fellow student "
                        "I am always happy to connect. I am particularly interested in internship opportunities and "
                        "engineering challenges in the Namibian mining sector.",
                        size=14, color=MUTED, width=380,
                    ),
                    ft.Container(height=20),
                    ft.Column([
                        ft.Container(
                            content=ft.Row([ft.Text("📧", size=16), ft.Column([
                                ft.Text("EMAIL", size=10, color=MUTED, letter_spacing=1.5),
                                ft.Text("danieldanielm09@gmail.com", size=13, color=TEXT),
                            ], spacing=2)], spacing=12),
                            padding=ft.padding.all(14),
                            bgcolor=SURFACE,
                            border=ft.border.all(0.5, "#FFFFFF0A"),
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Row([ft.Text("📱", size=16), ft.Column([
                                ft.Text("CELL", size=10, color=MUTED, letter_spacing=1.5),
                                ft.Text("+264 81 716 0236", size=13, color=TEXT),
                            ], spacing=2)], spacing=12),
                            padding=ft.padding.all(14),
                            bgcolor=SURFACE,
                            border=ft.border.all(0.5, "#FFFFFF0A"),
                            border_radius=10,
                        ),
                        ft.Container(
                            content=ft.Row([ft.Text("📍", size=16), ft.Column([
                                ft.Text("LOCATION", size=10, color=MUTED, letter_spacing=1.5),
                                ft.Text("Ongwediva, Namibia", size=13, color=TEXT),
                            ], spacing=2)], spacing=12),
                            padding=ft.padding.all(14),
                            bgcolor=SURFACE,
                            border=ft.border.all(0.5, "#FFFFFF0A"),
                            border_radius=10,
                        ),
                    ], spacing=10),
                ], expand=True),
                ft.Container(width=60),
                ft.Column([
                    ft.TextField(label="Your name", border_color="#FFFFFF22", focused_border_color=GOLD,
                                 label_style=ft.TextStyle(color=MUTED), color=TEXT, bgcolor=SURFACE, border_radius=8),
                    ft.TextField(label="Your email", border_color="#FFFFFF22", focused_border_color=GOLD,
                                 label_style=ft.TextStyle(color=MUTED), color=TEXT, bgcolor=SURFACE, border_radius=8),
                    ft.TextField(label="Subject", border_color="#FFFFFF22", focused_border_color=GOLD,
                                 label_style=ft.TextStyle(color=MUTED), color=TEXT, bgcolor=SURFACE, border_radius=8),
                    ft.TextField(label="Message", border_color="#FFFFFF22", focused_border_color=GOLD,
                                 label_style=ft.TextStyle(color=MUTED), color=TEXT, bgcolor=SURFACE,
                                 border_radius=8, multiline=True, min_lines=4, max_lines=6),
                    ft.ElevatedButton(
                        "Send Message ✦",
                        bgcolor=GOLD, color=BG, width=220,
                        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
                    ),
                ], spacing=14, expand=True),
            ], vertical_alignment=ft.CrossAxisAlignment.START),
        ], spacing=0),
        padding=ft.padding.symmetric(horizontal=80, vertical=80),
        bgcolor=BG,
    )

    # ── FOOTER ───────────────────────────────────────────────────────────────
    footer = ft.Container(
        content=ft.Row([
            ft.Text("© 2026 ", size=12, color=MUTED),
            ft.Text("DANIEL MATHEW", size=12, color=GOLD, weight=ft.FontWeight.W_600),
            ft.Text(" — Mining Engineering, UNAM · Ongwediva, Namibia", size=12, color=MUTED),
            ft.Container(expand=True),
            ft.Text("Built with ♥ in Namibia", size=12, color=MUTED),
        ], spacing=2),
        padding=ft.padding.symmetric(horizontal=80, vertical=24),
        border=ft.border.only(top=ft.BorderSide(0.5, "#FFFFFF0F")),
        bgcolor=BG,
    )

    # ── ASSEMBLE ─────────────────────────────────────────────────────────────
    page.add(
        ft.Stack([
            ft.Column([
                nav,
                hero,
                about,
                timeline_section,
                matlab_section,
                blog_section,
                github_section,
                contact_section,
                footer,
            ], spacing=0, scroll=ft.ScrollMode.AUTO),
        ]),
    )


ft.app(target=main, view=ft.AppView.WEB_BROWSER, port=8080)
