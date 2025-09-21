# Module 5: Working with Media, Files & Advanced Inputs

### Topic 5.1: Date Input
<br>

#### **Introduction**

Date handling is essential for many applications—from project management tools to event planning systems. Users need intuitive ways to select dates, and apps need to perform calculations with those dates. Streamlit's `st.date_input()` provides an elegant calendar widget that makes date selection simple and user-friendly.

The `st.date_input()` function creates an interactive calendar picker that returns Python `datetime.date` objects. These objects can be used with Python's `datetime` module to perform powerful date calculations, comparisons, and formatting operations that drive dynamic app behaviors.

Working with dates opens up possibilities for countdown timers, scheduling applications, deadline trackers, and any app where time-based calculations create value for users.

#### **Mini Project**

You want to know exactly how many days until your next birthday so you can plan celebrations or just enjoy the anticipation. This birthday countdown app lets you select your birth date and automatically calculates how many days remain until your special day arrives.

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

Date input widgets paired with Python's datetime tools transform complex temporal calculations into simple, elegant solutions. These technologies work together to create applications that don't just handle dates—they bring time to life through personalized, interactive experiences that resonate with users. The seamless integration of user-friendly interfaces with powerful backend processing demonstrates how modern web applications can make sophisticated time-based functionality accessible to everyone.

----

### Topic 5.2: Color Input
<br>

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

File handling capabilities transform static applications into dynamic data processing tools. Users often have data stored in files that they need to analyze, process, or transform. Streamlit's `st.file_uploader()` enables users to upload files directly into your app, while `st.download_button()` allows them to download processed results.

The `st.file_uploader()` function creates a drag-and-drop interface that accepts various file types and returns file objects that can be processed immediately. Combined with `st.download_button()`, you can create complete data processing workflows where users upload raw data and download refined results.

These file handling capabilities enable you to build practical applications for data analysis, document processing, and any scenario where users need to work with their own files rather than static demo data.

#### **Mini Project**

You want to analyze your monthly spending habits but your bank exports data as a CSV file that's difficult to read. You need a tool that can upload your expense CSV, show you a preview of the data, calculate spending totals by category, and let you download a clean summary for your records.

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

-  We use the **pandas** library, a powerful Python toolkit for data manipulation and analysis. It provides DataFrame objects, which are like tables in a spreadsheet, making it easy to read, process, and summarize tabular data. Here, we use it to read the CSV file, preview the data, and calculate category totals.
    
-   The `st.file_uploader()` function creates a drag-and-drop interface for uploading files. The `type="csv"` parameter ensures that only CSV files can be uploaded, helping prevent format errors.
    
-  When a file is uploaded, `uploaded_file` becomes a file-like object. We pass it directly to `pd.read_csv()` to convert it into a pandas DataFrame. The check `if uploaded_file is not None:` ensures that we only attempt to read the file after an upload occurs.
    
-   `df.head(10)` displays the first 10 rows of the uploaded file. Using `st.dataframe()` provides an interactive table so users can quickly verify the uploaded data.
    
-  We calculate total spending per category using pandas `groupby()` and `sum()`. The conditional check `if 'category' in df.columns and 'amount' in df.columns:` ensures the expected columns exist before performing calculations, preventing errors.
    
-  The `st.download_button()` function allows users to download the processed summary. `category_totals.to_csv(index=False)` converts the DataFrame to CSV format without row indices. The `mime="text/csv"` parameter tells the browser to treat the file as a CSV for proper handling.
    
    -   **MIME (Multipurpose Internet Mail Extensions)** types are standardized labels that instruct browsers and apps how to process different file formats. Here, `"text/csv"` ensures the file opens correctly in spreadsheet applications.

---

#### **Key Learning Points**

-   `st.file_uploader()` accepts `type` parameters to restrict file formats and prevent upload errors

-   File objects from uploads can be used directly with pandas and other data processing libraries

-   Always check if files are uploaded before attempting to process them

-   `st.dataframe()` provides immediate visual feedback for uploaded data verification

-   `st.download_button()` requires data as string format and appropriate MIME types for proper downloads

#### **Conclusion**

File upload and download functionality transforms Streamlit applications from static tools into dynamic data processing platforms. By enabling users to bring their own data, analyze it in real-time, and export refined results, you create self-contained workflows that integrate seamlessly into existing business processes across industries—from financial reporting to scientific research.

-----

### Topic 5.4: Images

<br>

#### **Introduction**

Streamlit apps can do more than display data—they can become interactive visual tools that manipulate, enhance, and transform images in real time. With the `st.image()` function, you can effortlessly show images from files, URLs, PIL objects, or even numpy arrays, making it ideal for both original and processed visuals.

When paired with image processing libraries, your app can create striking before-and-after comparisons, apply creative filters, or perform specialized tasks. These capabilities open the door to building practical and fun tools for photography, design, content creation, or any scenario where users want to interact with and process images directly within your app.


#### **Mini Project**

You need a quick tool to clean up photos for professional use by removing backgrounds from ID photos, product images, or profile pictures. The app should let you upload an image, automatically remove the background using AI, show a side-by-side comparison, and download the processed result.

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


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/image1mod5.png">


<img src="https://github.com/smaranjitghose/streamlit_course/blob/master/images/Module%205/iamge2mod5.png">

----

#### **Step-by-Step Walkthrough**


        
-   **PIL (Python Imaging Library)**: Handles image loading and manipulation. `Image.open()` converts uploaded files into Image objects suitable for display and processing.
        
-   **`rembg`**: A Python library that uses pre-trained AI models to automatically detect and remove image backgrounds. No manual selection or green screen is needed.
        
-   **`io`**: Handles in-memory binary streams to convert processed images into a format suitable for display and download.

-   The `st.file_uploader()` function allows users to upload images with specific extensions (png, jpg, jpeg) to ensure that only compatible files are processed.       

-   `rembg.remove(img_bytes)` removes the background using AI-powered models.
        
-  The `st.spinner()` function in Streamlit is a context manager that provides visual feedback to users while the app is performing a time-consuming task.
    
-   The processed image is saved to a `BytesIO` buffer in **PNG format**, which preserves transparency.
        
---

#### **Conclusion**

By bridging powerful image processing libraries with Streamlit's user-friendly interface, you can make advanced AI capabilities accessible to non-technical users who need professional-grade results. This pattern extends beyond background removal to any image manipulation task—from style transfer to object detection to medical imaging analysis—where the complexity of the underlying technology is hidden behind elegant simplicity.


-----

### Topic 5.5: Audio

<br>

#### **Introduction**

Audio handling brings your Streamlit apps to life, letting users interact with voice recordings, music, and other sound files directly in the browser. With `st.audio()`, you can effortlessly embed an audio player that lets users play, pause, and navigate through their audio content.

The function is flexible—it accepts uploaded files, byte data, or file paths—making it easy to display both user-provided recordings and programmatically generated audio. Common formats like WAV and MP3 are fully supported, ensuring broad compatibility across devices.

While Streamlit doesn't have built-in audio recording capabilities, you can create audio processing workflows where users upload audio files, process them with Python libraries, and download the results, creating practical tools for audio analysis and manipulation.

#### **Mini Project**

You want to create a simple voice memo tool that lets you upload short audio recordings, play them back to review the content, for sharing or archiving. This demonstrates how to handle audio files in Streamlit applications.

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

By combining Streamlit's interface capabilities with robust audio processing libraries, you create versatile platforms that adapt to diverse audio workflows—from podcast production and voice note organization to acoustic analysis and sound quality enhancement. These applications eliminate the complexity of command-line audio tools while maintaining the power and flexibility that professional audio work demands.


---

### Topic 5.6: Camera Access

<br>

#### **Introduction**

Imagine being able to snap a photo right inside a web app — no separate camera app, no extra steps. That’s exactly what Streamlit’s `st.camera_input()` makes possible. With just a single click, users can capture images directly from their browser, instantly turning them into digital objects your app can work with.

The photos returned by `st.camera_input()` are ready for immediate processing, opening the door to applications like profile creation, document verification, or any workflow that needs fresh, live images.

By adding camera input, you transform a static app into an interactive, creative tool—one that can generate personalized content, build custom graphics, or handle real-time visual data—all from within the browser itself.

#### **Mini Project**

You need a simple tool to create basic ID cards for events, workshops, or small organizations. The app should let you take a photo using your device camera, add your name and ID number as text overlay, and download the finished ID card for printing or sharing.

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

Camera functionality in Streamlit creates seamless workflows where users can capture, process, and generate personalized content without leaving the application. This real-time approach eliminates the friction of file uploads while enabling sophisticated applications like document verification systems, personalized marketing materials, or interactive kiosks that respond immediately to user interaction.

----

### Topic 5.7: Video

<br>

#### **Introduction**

Videos bring apps to life, letting users see information in motion rather than just reading or clicking. With Streamlit’s `st.video()`, you can embed videos that play directly in the browser, complete with familiar controls like play, pause, seek, volume, and fullscreen.

The function is versatile—it works with uploaded files, byte streams, or even URLs—so you can display anything from short clips to full-length tutorials. Supported formats like **MP4**, **MOV**, and **WebM** ensure your videos run smoothly across devices.

Adding video playback isn’t just about showing media; it opens up possibilities for interactive learning, content previews, or multimedia dashboards—anywhere seeing motion enhances understanding or engagement.

#### **Mini Project**

You want to create a simple video player that lets you upload movie trailers or promotional videos and watch them with full playback controls. This demonstrates how to handle video file uploads and display them for immediate viewing within your Streamlit application.

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

bash

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

By combining intuitive video upload with instant playback capabilities, Streamlit applications become complete media processing environments where users can review, organize, and manage video content without switching between multiple tools. This seamless integration supports diverse applications from content creation pipelines to educational platforms, making professional video handling accessible through simple web interfaces.


----

### Topic 5.8: PDFs

<br>

#### **Introduction**

Imagine opening a PDF and being able to explore its pages right inside your app—no extra software, no switching tabs. Streamlit lets you turn static PDF documents into interactive experiences where you can skim through pages, read text, and preview content instantly. Streamlit provides built-in PDF display capabilities alongside powerful text extraction tools.

The combination of Streamlit's PDF display functions with libraries enables comprehensive document processing workflows. Users can upload PDFs, view them inline, extract metadata like page counts, and pull text content for analysis or processing.

PDF processing capabilities enable applications for document review, content analysis, research tools, and any scenario where users need to work with PDF documents as part of their data workflow.

#### **Mini Project**

You need a quick tool to preview PDF documents before sharing them with colleagues or clients. The app should let you upload a PDF, show basic information like filename and page count, extract a text snippet from the first page for quick review, and display the full document for thorough examination.

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

Streamlit's PDF capabilities bridge the gap between document-heavy workflows and modern web applications, enabling users to upload, analyze, and extract value from PDFs without leaving their browser. This foundation scales from basic document viewers to comprehensive processing pipelines that handle batch analysis, content summarization, and automated data extraction for legal, academic, and business applications.