import os
import glob
from utils.logger import CustomLogger

logger = CustomLogger.get_logger()

class ReportCleanupUtils:
    """Utility class to manage and clean up old HTML report files."""

    @staticmethod
    def cleanup_old_reports(report_dir="reports/html", keep_count=5):
        """Scans the report directory and keeps only the latest 'keep_count' HTML files."""
        try:
            if not os.path.exists(report_dir):
                return

            # Find all html report files in the folder
            search_path = os.path.join(report_dir, "report_*.html")
            report_files = glob.glob(search_path)

            # Sort files by modification time (oldest first)
            report_files.sort(key=os.path.getmtime)

            # Check if total files exceed the allowed limit
            if len(report_files) > keep_count:
                files_to_delete = report_files[:-keep_count]
                for file_path in files_to_delete:
                    os.remove(file_path)
                    logger.info(f"🧹 Cleaned up old HTML report: {file_path}")

        except Exception as e:
            logger.error(f"❌ Failed during report cleanup: {e}")