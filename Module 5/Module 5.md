# Module 5: Working with Media, Files & Advanced Inputs

### Topic 5.1: Date Input
<br>

#### **Introduction**

Modern applications frequently require users to interact with time-sensitive data—whether scheduling meetings, tracking project deadlines, or planning events. However, manual date entry through text fields is error-prone and creates poor user experiences, while building custom calendar interfaces from scratch is complex and time-consuming. Streamlit's `st.date_input()` addresses these challenges by providing an elegant calendar widget that transforms complex date selection into a simple, user-friendly interaction.

The `st.date_input()` function creates an interactive calendar picker that returns Python datetime.date objects, seamlessly integrating with Python's powerful datetime module for calculations, comparisons, and formatting operations. This functionality enables developers to build sophisticated time-based features like countdown timers, scheduling applications, deadline trackers, and any application where date calculations create meaningful value for users, all while maintaining the intuitive user experience that modern applications demand.

#### **Mini Project**

Alex loves birthdays and always gets excited weeks in advance, but constantly finds himself trying to calculate how many days are left until his special day. He'll count on calendars, ask friends to help him figure it out, or just guess and wonder if he's getting the math right. The anticipation is half the fun, but not knowing exactly when to start planning parties or getting genuinely excited is frustrating.
A birthday countdown app would turn this guesswork into pure excitement, giving Alex the precise countdown he craves to make every day leading up to his birthday feel special.

##### **Project Setup**

Create a new file `app.py`:

python

```python
import streamlit as st
from datetime import date, datetime

st.title("🎂 Birthday Countdown")

# Date selection for birthday
birth_date = st.date_input("When is your birthday?")

# Calculate days until next birthday
today = date.today()
this_year_birthday = birth_date.replace(year=today.year)

# If birthday already passed this year, calculate for next year
if this_year_birthday < today:
    next_birthday = birth_date.replace(year=today.year + 1)
else:
    next_birthday = this_year_birthday

days_until = (next_birthday - today).days

# Display countdown
if days_until > 0:
    st.metric("Days Until Birthday", days_until)
    st.success(f"🎉 Only {days_until} days until your birthday!")
elif days_until == 0:
    st.balloons()
    st.success("🎊 Happy Birthday! Today is your special day!")
```

**Run your app with:**


```bash
streamlit run app.py
```

##### **Output**


<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/bdaymod5.png">

----

#### **Step-by-Step Walkthrough**

- The `st.date_input()` function creates a calendar widget where users can select their birthday by clicking on calendar days or typing the date directly.

- The birthday calculation logic handles the complexity of determining the next occurrence of a birthday. It creates a birthday date for the current year, then checks if that date has already passed. If so, it calculates the birthday for next year instead.

- The date subtraction (`next_birthday - today`) returns a `timedelta` object, and accessing its `.days` attribute gives the number of days as an integer for the countdown display.

- The `st.success()`  function provides a green-colored status message that creates positive, celebratory feedback. Streamlit offers several status message functions including `st.success()` for positive messages (green), `st.info()` for informational messages (blue), `st.warning()` for caution messages (yellow), and `st.error()` for error messages (red).

---

#### **Conclusion**

Date input widgets combined with datetime processing libraries represent essential patterns for handling temporal data across web development frameworks and desktop applications. These integration techniques enable developers to build sophisticated time-aware systems that power everything from scheduling platforms to analytics dashboards with intuitive user experiences. The seamless connection between user-friendly interfaces and robust temporal calculations forms the foundation for creating applications that make complex time-based operations accessible and meaningful to end users.

----

### Topic 5.2: Color Input


#### **Introduction**

Color selection is essential for design tools, brand development, and any application where visual consistency matters. Designers and marketers need efficient ways to create, preview, and share color palettes without switching between multiple tools. Streamlit's `st.color_picker()` provides an intuitive color selection interface that returns hex color codes for immediate use.

The `st.color_picker()` function creates a visual color picker with familiar interfaces—color wheels, sliders, and direct hex input. The widget returns hex color strings that can be applied to styling, exported as data, or used to generate visual previews of color combinations.

Color input capabilities enable you to build professional design tools, brand palette generators, and customization interfaces that provide immediate visual feedback and practical output formats.

#### **Mini Project**

You're a freelance designer who needs a quick tool to create brand color palettes for clients. The tool should let you select three brand colors, display them as professional swatches with hex codes, and arrange them in a clean palette strip that clients can easily reference and approve.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("🎨 Brand Palette Creator")

# Color selection
color1 = st.color_picker("Primary Color", "#FF6B6B")
color2 = st.color_picker("Secondary Color", "#4ECDC4") 
color3 = st.color_picker("Accent Color", "#45B7D1")

# Display color codes
st.subheader("Your Brand Colors")
st.write(f"Primary: {color1}")
st.write(f"Secondary: {color2}")
st.write(f"Accent: {color3}")
```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**


<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/color1mod5.png">


<img src ="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/color2mod5.png">





---

#### **Step-by-Step Walkthrough**

- The `st.color_picker()` functions create three color selection widgets, each with descriptive labels and professional default colors. Each widget opens a color picker interface when clicked, allowing users to select colors visually or enter hex codes directly.

- The color pickers return hex color strings (like "`#FF6B6B`") that represent the selected colors. These strings can be used immediately for display, styling, or export purposes.

- The `st.write()` functions display the selected hex codes in a simple, readable format that users can easily copy for use in other design tools or applications.

---

#### **Conclusion**

Color input widgets unlock possibilities beyond mere selection—they enable experimentation, comparison, and real-time refinement. These tools transform color management from a static choice into a dynamic, interactive experience that enhances creative workflows and design processes. The immediate visual feedback and intuitive controls empower users to iterate quickly, explore color relationships, and make confident design decisions with unprecedented ease.


----

### Topic 5.3: File Upload & Download

<br>

#### **Introduction**

File handling capabilities transform static applications into dynamic data processing tools that work with real user data. Many applications require users to upload their own datasets, documents, or media files for processing, but traditional web development makes this complex and requires significant backend infrastructure. Streamlit's file handling widgets solve this challenge by providing simple, elegant interfaces that enable seamless data exchange between users and applications.

The `st.file_uploader()` function creates an intuitive drag-and-drop interface that accepts various file types and returns file objects for immediate processing. This capability enables developers to build practical applications for data analysis, document processing, report generation, and any scenario where users need to work with their own files rather than static demo data, transforming simple prototypes into fully functional data processing tools that handle real-world workflows.

#### **Mini Project**

Maya tries to stick to her monthly budget, but when she downloads her bank statement as a CSV file, she's faced with rows and rows of cryptic transaction codes and messy data that make no sense. She spends hours manually sorting through expenses, trying to figure out how much she spent on groceries versus dining out, often giving up halfway through and losing track of her spending patterns. Without clear insights into where her money actually goes, her budget plans always fall apart.

A spending analysis app would transform this confusing data chaos into clear, actionable insights that help Maya take control of her finances and make informed decisions about her spending habits.

##### **Project Setup**

Create a new file `app.py`:


```python
import streamlit as st
import pandas as pd

st.title("💰 CSV Expense Analyzer")

# File upload
uploaded_file = st.file_uploader("Upload your expense CSV file", type="csv")

if uploaded_file is not None:
    # Read and preview the data
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write("First 10 rows of your expenses:")
    st.dataframe(df.head(10))
    
    # Group by category and calculate totals
    if 'category' in df.columns and 'amount' in df.columns:
        st.subheader("Spending by Category")
        category_totals = df.groupby('category')['amount'].sum().reset_index()
        st.dataframe(category_totals)
        
        # Download summary
        csv_summary = category_totals.to_csv(index=False)
        st.download_button(
            "Download Summary CSV",
            data=csv_summary,
            file_name="expense_summary.csv",
            mime="text/csv"
        )
    else:
        st.warning("CSV must have 'category' and 'amount' columns")
else:
    st.info("Please upload a CSV file to begin analysis")
```

**Run your app with:**


```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/csv1mod5.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/csv2mod5.png">


-----

#### **Step-by-Step Walkthrough**

-   We use the **pandas** library, a powerful Python toolkit for data manipulation and analysis. It provides DataFrame objects, which are like tables in a spreadsheet, making it easy to read, process, and summarize tabular data. Here, we use it to read the CSV file, preview the data, and calculate category totals.
    
-   The `st.file_uploader()` function creates a drag-and-drop interface for uploading files. Its parameters include:
    
    -   `label`: Displays instructions to the user above the uploader.
        
    -   `type`: Restricts file uploads to specific types; here, `"csv"` ensures only CSV files can be uploaded.
        
    -   `accept_multiple_files`: Determines whether the user can upload multiple files; `False` allows only a single file.
        
    -   `key`: Optional unique identifier for the widget, useful if you have multiple uploaders in the same app.
        
    -   `help`: Optional tooltip or guidance text displayed when the user hovers over the uploader.
        
-   When a file is uploaded, `uploaded_file` becomes a file-like object. We pass it directly to `pd.read_csv()` to convert it into a pandas DataFrame. The check `if uploaded_file is not None:` ensures that we only attempt to read the file after an upload occurs.
    
-   `df.head(10)` displays the first 10 rows of the uploaded file. Using `st.dataframe()` provides an interactive table so users can quickly verify the uploaded data.
    
-   We calculate total spending per category using pandas `groupby()` and `sum()`. The conditional check `if 'category' in df.columns and 'amount' in df.columns:` ensures the expected columns exist before performing calculations, preventing errors.
    
-   The `st.download_button()` function allows users to download the processed summary. `category_totals.to_csv(index=False)` converts the DataFrame to CSV format without row indices. The `mime="text/csv"` parameter tells the browser to treat the file as a CSV for proper handling.
    
    -   **MIME (Multipurpose Internet Mail Extensions)** types are standardized labels that instruct browsers and apps how to process different file formats. Here, `"text/csv"` ensures the file opens correctly in spreadsheet applications.

---


#### **Conclusion**

File upload and download capabilities represent core functionality that transforms any application into a comprehensive data processing platform across web, desktop, and enterprise environments. These patterns enable developers to create self-contained workflows where users can import data, perform real-time analysis, and export results, making applications immediately valuable to end users. The ability to handle bidirectional file operations is essential for building professional-grade applications that integrate seamlessly into real-world business processes and workflows.

-----

### Topic 5.4: Images

<br>

#### **Introduction**

Streamlit apps can do more than display data—they can become interactive visual tools that manipulate, enhance, and transform images in real time. With the `st.image()` function, you can effortlessly show images from files, URLs, PIL objects, or even numpy arrays, making it ideal for both original and processed visuals.

When paired with image processing libraries, your app can create striking before-and-after comparisons, apply creative filters, or perform specialized tasks. These capabilities open the door to building practical and fun tools for photography, design, content creation, or any scenario where users want to interact with and process images directly within your app.


#### **Mini Project**

Marcus runs a small online business and constantly needs product photos with clean, white backgrounds for his website and social media. Every time he takes photos, he faces the same frustrating problem: messy backgrounds that make his products look unprofessional. He's tried editing apps before, but manually selecting and erasing backgrounds takes forever and never looks quite right, leaving him with jagged edges and obvious mistakes that hurt his brand image.
A background removal app would eliminate this tedious editing process and give Marcus the professional-looking product photos he needs to present his business confidently.

##### **Project Setup**

First, install the required library:


```bash
uv add rembg
```

Create a new file `app.py`:



```python
import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("🖼️ Background Remover")

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load and display original image
    original_image = Image.open(uploaded_file)
    
    st.subheader("Original Image")
    st.image(original_image, width=300)
    
    # Process image to remove background
    with st.spinner("Removing background..."):
        # Convert to bytes for rembg processing
        img_bytes = uploaded_file.getvalue()
        processed_bytes = remove(img_bytes)
        processed_image = Image.open(io.BytesIO(processed_bytes))
    
    st.subheader("Processed Image")
    st.image(processed_image, width=300)
    
    # Download processed image
    buf = io.BytesIO()
    processed_image.save(buf, format="PNG")
    
    st.download_button(
        "Download Processed Image",
        data=buf.getvalue(),
        file_name="background_removed.png",
        mime="image/png"
    )
else:
    st.info("Upload an image to remove its background")
```

**Run your app with:**


```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/bgremove1.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/bgremove2.png">

----

#### **Step-by-Step Walkthrough**


        
-   **PIL (Python Imaging Library)**: Handles image loading and manipulation. `Image.open()` converts uploaded files into Image objects suitable for display and processing.
    
-   **`rembg`**: A Python library that uses pre-trained AI models to automatically detect and remove image backgrounds. No manual selection or green screen is needed.
    
-   **`io`**: Handles in-memory binary streams to convert processed images into a format suitable for display and download.
    
-   The `st.file_uploader()` function allows users to upload images with specific extensions to ensure that only compatible files are processed. Its parameters include:
    
    -   `label`: Displays instructions to the user above the uploader.
        
    -   `type`: Specifies allowed file extensions; here, `["png", "jpg", "jpeg"]`.
        
    -   `accept_multiple_files`: Determines whether multiple files can be uploaded; default is `False`.
        
    -   `key`: Optional unique identifier for the widget.
        
    -   `help`: Optional tooltip or guidance text displayed when hovering over the uploader.
        
-   `Image.open(uploaded_file)` loads the uploaded image into a format that can be displayed with `st.image()` and processed with `rembg`.
    
-   The `st.spinner()` function in Streamlit is a context manager that provides visual feedback to users while the app is performing a time-consuming task, such as removing a background.
    
-   `rembg.remove(img_bytes)` removes the background from the image using AI-powered models.
    
-   The processed image is saved to a `BytesIO` buffer in **PNG format**, which preserves transparency.
    
-   `st.download_button()` allows users to download the processed image. Its parameters include:
    
    -   `label`: Text displayed on the download button.
        
    -   `data`: The file content to be downloaded, here taken from the `BytesIO` buffer.
        
    -   `file_name`: The default name for the downloaded file, e.g., `"background_removed.png"`.
        
    -   `mime`: The MIME type to specify the file format; here `"image/png"` ensures proper handling in browsers.
        
    -   `key`: Optional unique identifier for the widget.
        
---

#### **Conclusion**

By bridging powerful image processing libraries with Streamlit's user-friendly interface, you can make advanced AI capabilities accessible to non-technical users who need professional-grade results. This pattern extends beyond background removal to any image manipulation task—from style transfer to object detection to medical imaging analysis—where the complexity of the underlying technology is hidden behind elegant simplicity.


-----

### Topic 5.5: Audio

<br>

#### **Introduction**

Audio processing applications often require users to preview, analyze, or work with sound files, but embedding audio playback in web applications traditionally involves complex HTML5 audio implementations and cross-browser compatibility issues. Users need intuitive ways to interact with their audio content—whether voice recordings, music files, or generated sounds—without leaving the application interface. Streamlit's `st.audio()` widget eliminates these technical barriers by providing a simple, browser-native audio player that handles playback seamlessly.
The `st.audio()` function accepts uploaded files, byte data, or file paths, supporting common formats like WAV and MP3 for broad device compatibility. This flexibility enables developers to create comprehensive audio workflows where users can upload audio files, preview them instantly, and process them with Python libraries, transforming complex audio tasks into streamlined, user-friendly applications.

#### **Mini Project**

Jake loves discovering new podcasts and audio content online, but he's frustrated with how difficult it is to sample episodes before committing to a subscription or download. He finds interesting audio clips shared on social media and forums, but they're often embedded in websites with poor players that buffer constantly or don't work on his device. He wants to quickly listen to these audio samples to decide if they're worth his time, but the clunky web players make the experience more annoying than enjoyable.
A simple audio upload and playback app would let Jake easily listen to audio samples he finds online in a clean, reliable player without the frustration of broken website interfaces.

##### **Project Setup**

Create a new file `app.py`:


```python
import streamlit as st
import io

st.title("🎙️ Voice Memo Player")

# Audio file upload
uploaded_audio = st.file_uploader("Upload your voice memo", type=["wav", "mp3", "m4a"])

if uploaded_audio is not None:
    # Display audio player
    st.subheader("Your Voice Memo")
    st.audio(uploaded_audio)
    
    # Show file details
    st.write(f"File name: {uploaded_audio.name}")
    st.write(f"File size: {len(uploaded_audio.getvalue())} bytes")
    
    # Additional processing info
    st.info("Audio uploaded successfully! You can play it using the controls above.")
    
else:
    st.info("Upload an audio file to play your voice memo")
    st.write("Supported formats: WAV, MP3, M4A")
```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/audiomod5.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/audio2mod5.png">


----

#### **Step-by-Step Walkthrough**

-   `st.file_uploader()` is configured with `type=["wav", "mp3", "m4a"]` to restrict uploads to common audio formats. This ensures only compatible audio files can be processed and played.
      
    
-   `st.audio(uploaded_audio)` creates a browser-native audio player with built-in controls like play/pause, progress bar, and volume adjustment.
        
-   The uploaded audio file is used directly—no additional conversion or processing is required.

-   `uploaded_audio.name` retrieves the original filename of the uploaded audio.
        
-   `len(uploaded_audio.getvalue())` returns the file size in bytes.
    
-   Displaying this information gives users quick insight into the uploaded file.


---

#### **Conclusion**

The integration of user-friendly interfaces with powerful audio processing libraries creates versatile platforms that serve diverse multimedia workflows across web and desktop applications. These patterns eliminate the complexity of command-line tools while preserving professional-grade functionality, making sophisticated audio manipulation accessible to both technical and non-technical users. This approach to combining intuitive interfaces with powerful backend capabilities represents a fundamental design principle for creating applications that bring advanced technical functionality to mainstream users.


---

### Topic 5.6: Camera Access

<br>

#### **Introduction**

Imagine being able to snap a photo right inside a web app — no separate camera app, no extra steps. That’s exactly what Streamlit’s `st.camera_input()` makes possible. With just a single click, users can capture images directly from their browser, instantly turning them into digital objects your app can work with.

The photos returned by `st.camera_input()` are ready for immediate processing, opening the door to applications like profile creation, document verification, or any workflow that needs fresh, live images.

By adding camera input, you transform a static app into an interactive, creative tool—one that can generate personalized content, build custom graphics, or handle real-time visual data—all from within the browser itself.

#### **Mini Project**

Mark organizes monthly community workshops and always struggles with creating professional-looking ID badges for attendees. He usually ends up hand-writing names on generic stickers or printing plain labels, which look unprofessional and don't include photos for security. The local print shop charges too much for custom ID cards, and using complex design software takes hours he doesn't have. His events would run smoother with proper identification, but the current process is too time-consuming and expensive.
A simple ID card creator would solve this by letting Mark quickly generate professional-looking photo IDs for his events without the high costs or technical complexity.

##### **Project Setup**

First, install the required library:


```bash
uv add pillow
```

Create a new file `app.py`:

```python
import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.title("📷 ID Card Maker")

# Camera input
photo = st.camera_input("Take your ID photo")

if photo is not None:
    # Convert to PIL Image
    image = Image.open(photo)
    
    # Get user details
    name = st.text_input("Enter your name")
    id_number = st.text_input("Enter ID number")
    
    if name and id_number:
        # Create ID card
        # Resize photo to standard size
        image = image.resize((300, 400))
        
        # Create new image for ID card
        card_width, card_height = 500, 300
        card = Image.new('RGB', (card_width, card_height), 'white')
        
        # Paste photo on left side
        photo_resized = image.resize((150, 200))
        card.paste(photo_resized, (20, 50))
        
        # Add text
        draw = ImageDraw.Draw(card)
        
        # Add name
        draw.text((200, 80), f"Name: {name}", fill='black')
        
        # Add ID number  
        draw.text((200, 120), f"ID: {id_number}", fill='black')
        
        # Add title
        draw.text((200, 40), "ID CARD", fill='blue')
        
        # Display the ID card
        st.subheader("Your ID Card")
        st.image(card)
        
        # Download functionality
        buf = io.BytesIO()
        card.save(buf, format="PNG")
        
        st.download_button(
            "Download ID Card",
            data=buf.getvalue(),
            file_name=f"id_card_{name.replace(' ', '_')}.png",
            mime="image/png"
        )
    
else:
    st.info("Take a photo to create your ID card")
```

**Run your app with:**


```bash
streamlit run app.py
```

##### **Output**

<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/cameramod51.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/cameramod52.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/cameramod53.png">


---

#### **Step-by-Step Walkthrough**


 -  **Pillow (PIL)**: Python’s most popular image processing library. It provides tools to open, manipulate, and save images in various formats. In this app, PIL is used for:

	-   Converting captured camera photos into editable Image objects (`Image.open()`)
	    
	-   Resizing images (`resize()`)
	    
	-   Creating new image canvases (`Image.new()`)
	    
	-   Adding text overlays (`ImageDraw.Draw()`)

- **Camera Input**: `st.camera_input()` opens the device camera and captures a photo, returning it as an image file object.

- **Creating the ID Card Layout:** The captured photo is resized, pasted onto a new white background canvas, and positioned on the left side of the ID card.

- **Adding Text**: `ImageDraw.Draw()` overlays text for the title, name, and ID number at specific coordinates with chosen colors.


---


#### **Conclusion**

Camera functionality integrated with web applications creates seamless workflows where users can capture, process, and generate personalized content without external tools or file transfers. This real-time approach eliminates upload friction while enabling sophisticated applications like document verification systems, interactive kiosks, and automated content generation platforms. These patterns represent essential capabilities for building modern applications that require immediate visual input processing and can adapt instantly to user-generated content.

----

### Topic 5.7: Video

<br>

#### **Introduction**

Modern applications increasingly rely on video content to convey complex information, demonstrate processes, or engage users through rich media experiences. However, implementing video playback in web applications traditionally requires handling multiple formats, browser compatibility issues, and custom player controls, creating significant development overhead. Streamlit's `st.video()` widget simplifies this complexity by providing a robust, browser-native video player with familiar controls like play, pause, seek, volume, and fullscreen capabilities.
The `st.video()` function works seamlessly with uploaded files, byte streams, or URLs, supporting formats like **MP4**, **MOV**, and **WebM** to ensure smooth playback across devices. 

#### **Mini Project**

Alok is a film enthusiast who downloads movie trailers and promotional videos from various sources to build his personal collection, but his computer's default video player is frustrating to use. The interface is cluttered with features he doesn't need, it takes forever to load, and sometimes it doesn't even support certain video formats he's downloaded. He just wants a clean, simple way to watch his trailer collection without dealing with buggy software or compatibility issues that interrupt his viewing experience.
A streamlined video player would give Alok the smooth, hassle-free viewing experience he wants for his personal video collection without the bloat and technical problems of complicated media software.

##### **Project Setup**

Create a new file `app.py`:

```python
import streamlit as st

st.title("🎬 Video Trailer App")

# Video file upload
uploaded_video = st.file_uploader("Upload your video trailer", type=["mp4", "mov", "avi"])

if uploaded_video is not None:
    # Display video player
    st.subheader("Video Player")
    st.video(uploaded_video)
    
    # Show file details
    st.subheader("Video Details")
    st.write(f"File name: {uploaded_video.name}")
    st.write(f"File size: {len(uploaded_video.getvalue())} bytes")
    
    
    st.success("Video uploaded successfully! Use the player controls to watch your trailer.")
    
else:
    st.info("Upload a video file to start watching")
    st.write("Supported formats: MP4, MOV, AVI")
```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/vid1mod5.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/vid2mod5.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/video3mod5.png">


----

#### **Step-by-Step Walkthrough**

-   `st.file_uploader()` is configured with `type=["mp4", "mov", "avi"]` to restrict uploads to common video formats, ensuring compatibility with the built-in video player.
        
 -   `st.video(uploaded_video)` creates a browser-native HTML5 video player with controls such as play/pause, progress bar, volume adjustment, and fullscreen. The uploaded video plays directly without conversion.
        
 -   `uploaded_video.name` retrieves the original filename.

 -   `len(uploaded_video.getvalue())` calculates the file size in bytes, giving users quick insight into their uploaded video.

---

#### **Conclusion**

The combination of intuitive video upload and instant playback capabilities establishes essential patterns for building comprehensive media processing environments across web and desktop platforms. These integration techniques eliminate the need for multiple specialized tools, making professional-grade media workflows accessible to users regardless of technical expertise. This approach opens possibilities for creating powerful content management systems and multimedia processing tools that serve diverse industries with unified, user-friendly interfaces.


----

### Topic 5.8: PDFs

<br>

#### **Introduction**

PDF documents are ubiquitous in professional workflows—from reports and research papers to forms and legal documents—but working with them in web applications traditionally requires users to download files or switch between multiple applications to view content. This fragmented experience slows down productivity and creates barriers in data processing workflows where PDF content needs to be analyzed, searched, or transformed. Streamlit eliminates these friction points by providing built-in PDF display capabilities that allow users to interact with documents directly within the application interface.

Streamlit's PDF display functions enable comprehensive document processing workflows where users can upload PDFs, view them inline with page navigation, extract metadata like page counts, and pull text content for further analysis.

#### **Mini Project**

Lisa works at a law firm where she constantly deals with lengthy legal documents, but she only needs specific pages from these massive PDFs for different cases. Instead of sending entire 50-page contracts to clients when they only need to see page 12, she wastes time opening heavy PDF editors, navigating through dozens of pages, and trying to extract just the sections she needs. Her clients get frustrated receiving unnecessary pages, and she spends too much time on what should be a simple task.
A PDF preview and extraction app would let Lisa quickly browse through documents, identify the exact pages she needs, and download only those specific pages to share with clients efficiently.

##### **Project Setup**

First, install the required library:

```bash
uv add PyPDF2
```

Create a new file `app.py`:

```python
import streamlit as st
import PyPDF2
import io

st.title("📄 PDF Quick Preview")

# PDF file upload
uploaded_pdf = st.file_uploader("Upload a PDF document", type="pdf")

if uploaded_pdf is not None:
    # Read PDF with PyPDF2
    pdf_reader = PyPDF2.PdfReader(uploaded_pdf)
    num_pages = len(pdf_reader.pages)

    # Show metadata
    st.subheader("Document Information")
    st.write(f"Filename: {uploaded_pdf.name}")
    st.write(f"Number of pages: {num_pages}")

    # Page selection input
    page_number = st.number_input(
        "Enter page number to preview",
        min_value=1,
        max_value=num_pages,
        value=1,
        step=1
    )

    # Extract selected page text
    selected_page = pdf_reader.pages[page_number - 1]
    text_content = selected_page.extract_text() or "⚠️ No text found on this page."

    st.subheader(f"Page {page_number} Preview")
    preview_text = text_content[:500] + "..." if len(text_content) > 500 else text_content
    st.text_area("Text Preview", preview_text, height=200)

    pdf_writer = PyPDF2.PdfWriter()
    pdf_writer.add_page(selected_page)

    pdf_bytes = io.BytesIO()
    pdf_writer.write(pdf_bytes)
    pdf_bytes.seek(0)

    st.download_button(
        f"Download Page {page_number}",
        data=pdf_bytes,
        file_name=f"{uploaded_pdf.name.replace('.pdf','')}_page_{page_number}.pdf",
        mime="application/pdf"
    )

else:
    st.info("Upload a PDF file to preview its content")

```

**Run your app with:**

```bash
streamlit run app.py
```

##### **Output**


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/pdf1mod5.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/mod5pdf2.png">



<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/mod5pdf3.png">


---


#### **Step-by-Step Walkthrough**

- **PyPDF2**: A Python library for reading, manipulating, and extracting information from PDF documents. It allows access to PDF structure, text extraction, metadata, and page-level operations without external dependencies.

-   `PyPDF2.PdfReader(uploaded_pdf)` creates a reader object for accessing the PDF structure.
    
-   `len(pdf_reader.pages)` retrieves the total number of pages, while `uploaded_pdf.name` provides the original filename.

-  `pdf_reader.pages[page_number - 1].extract_text()` extracts the text from the selected page. If no text is found, a warning message is shown.
    
-   `st.text_area()` displays the extracted text in a scrollable box. The preview is truncated for readability if it exceeds 500 characters.

- `PyPDF2.PdfWriter()` creates a new PDF containing only the selected page.
---


#### **Conclusion**

PDF processing capabilities integrated with web interfaces bridge the gap between document-heavy workflows and modern application design, enabling seamless document analysis without external tools. These patterns scale from basic document viewers to comprehensive processing pipelines that handle batch analysis, content extraction, and automated data processing across industries. This approach represents a key strategy for digitizing traditional workflows and creating value-added services around content analysis and extraction.