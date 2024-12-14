require('dotenv').config();
const express = require('express');
const nodemailer = require('nodemailer');
const path = require('path');

const app = express();
app.use(express.json());
app.use(express.static('public'));

const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: process.env.EMAIL_USER,
        pass: process.env.EMAIL_APP_PASSWORD
    }
});

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/send-email', async (req, res) => {
    try {
        const { startDate, endDate, location, food } = req.body;

        const mailOptions = {
            from: process.env.EMAIL_USER,
            to: 'nguyhonglong2002@gmail.com',
            subject: 'Lời mời đi chơi',
            text: `
                Xin chào!
                
                Mình muốn mời bạn đi chơi:
                Thời gian: từ ${startDate} đến ${endDate}
                Địa điểm: ${location}
                Món ăn: ${food}
                
                Mong được phản hồi từ bạn!
            `
        };

        await transporter.sendMail(mailOptions);
        res.status(200).json({ message: 'Email sent successfully' });
    } catch (error) {
        console.error('Error sending email:', error);
        res.status(500).json({ error: 'Failed to send email' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});